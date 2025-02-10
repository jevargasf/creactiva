from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest, Http404, HttpResponseRedirect
from suscripciones.forms import SolicitudOrganizacionForm, SuscripcionOrganizacionForm, ElegirOrganizacionForm
from suscripciones.models import SolicitudOrganizacion, Suscripcion, CursosSuscripcion, PerfilSuscripcion, Planes
from suscripciones.utils import str_to_list, sumar_fecha
from django.contrib import messages
from main.models import User, Perfil
from cursos.models import Curso
from django.utils.timezone import now
from suscripciones.webpay import crear_transaccion, confirmar_transaccion
from suscripciones.services import suscripcion_usuario

# Create your views here.
class PlanesView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        
        return render(request, 'elegir_tipo.html')
    
class PlanIndividual(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        planes = Planes.objects.all()
        context = {
            'planes': planes
        }
        return render(request, 'plan_individual.html', context)

class DetallePlan(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest, id_plan):
        plan = Planes.objects.get(pk=id_plan)
        context = {
            'plan': plan
        }
        return render(request, 'detalle_plan.html', context)
    

    # ACÁ SE INICIA LA TRANSACCIÓN: CREAR TRANSACCIÓN
    def post(self, request: HttpRequest, id_plan):
        pass
class PagarView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        return render(request, 'pantalla_compra.html')
    
    def post(self, request: HttpRequest, id_plan):
        try:
            # AHORA SÍ ME SIRVE LA LÓGICA IF SUSCRIPCIÓN EXISTE, ENTONCES RECUPERAR, SI NO, CREAR
            suscripcion = suscripcion_usuario(request.user)
            if suscripcion is None:
                plan = Planes.objects.get(pk=id_plan)
                fecha_termino = sumar_fecha(plan.duracion)
                suscripcion = Suscripcion(
                    fecha_inicio=now(),
                    # fecha término es now + duración de la suscripción
                    fecha_termino=fecha_termino,
                    monto=plan.monto,
                    numero_usuarios=1,
                    codigo_validacion='0',
                    estado_suscripcion='2'
                )
                suscripcion.save()
                cursos = Curso.objects.all()
                for curso in cursos:
                    curso_suscripcion = CursosSuscripcion(
                        suscripcion=suscripcion,
                        curso=curso
                    )
                    curso_suscripcion.save()

                user_object = User.objects.get(username=request.user)
                perfil_object = Perfil.objects.get(user_id=user_object.id)
                perfil_suscripcion = PerfilSuscripcion(
                    perfil=perfil_object,
                    suscripcion=suscripcion
                )
                perfil_suscripcion.save()
                


            # ESTO SE GUARDA EN LA TABLA, PERO SOLO CUANDO LA TRANSACCIÓN ESTÁ CONFIRMADA SE HACE EFECTIVA
            # VOY A HACERLA EFECTIVA PASANDO EL ESTADO A 1
            # INICIALMENTE, SERÁ 0
            

            # CREAR TRANSACCIÓN 
            respuesta = crear_transaccion(suscripcion.id, plan.monto)
            #messages.success(request, 'Tu suscripción se ha procesado con éxito.')
            #return redirect('index')
            context = {
                'url': respuesta['url'],
                'token': respuesta['token']
            }
            print(context)
            return render(request, 'webpay.html', context)
        except User.DoesNotExist as e:
            print(f"Error: {e}")
            messages.error(request, 'Por favor, ingresa antes de continuar.')
            return redirect('login')
        except Exception as e:
            print(f"Error: {e}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
            messages.error(request, 'No se ha podido registrar la suscripción. Por favor, intenta nuevamente.')
            return redirect('plan-individual')

    
class RespuestaWebpayView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        if not request.GET.get('token_ws'):
            raise Http404
        token = request.GET.get('token_ws')
        result = confirmar_transaccion(token)
        if result[0] == 'vacio':
            raise Http404
        elif result[0] == 'AUTHORIZED':
            try:
                # reescribir la suscripción con la data
                suscripcion = suscripcion_usuario(request.user)
                # fecha_inicio = now()
                # fecha_termino = sumar_fecha(fecha_inicio)
                suscripcion.estado_transbank=result[0]
                suscripcion.tarjeta=result[1]
                suscripcion.fecha_transbank=result[2]
                suscripcion.token_ws=token
                suscripcion.estado_suscripcion='1'
                suscripcion.save()
                messages.success(request, 'Tu suscripción ha sido procesada con éxito.')
                context = {
                    'orden_compra': suscripcion.id,
                    'fecha_inicio': suscripcion.fecha_inicio,
                    'fecha_termino': suscripcion.fecha_termino,
                    'tarjeta': result[1],
                    'monto': suscripcion.monto
                }
                return render(request, 'voucher_webpay.html', context)
            except Exception as e:
                print(f"Error: {e}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
                raise Http404
            # crear el html de la respuesta o armar el context
            # enviar correos de confirmación
            
            # retornar
        elif result[0] == 'FAILED':
            try:
                # reescribir la suscripción con la data
                suscripcion = suscripcion_usuario(request.user)
                # fecha_inicio = now()
                # fecha_termino = sumar_fecha(fecha_inicio)
                suscripcion.estado_transbank=result[0]
                suscripcion.tarjeta=result[1]
                suscripcion.fecha_transbank=result[2]
                suscripcion.token_ws=token
                suscripcion.estado_suscripcion='2'
                suscripcion.save()
                messages.error(request, 'Lo sentimos, ocurrió un error. Por favor, intenta nuevamente.')
                context = {
                    'orden_compra': suscripcion.id,
                    'fecha_inicio': suscripcion.fecha_inicio,
                    'fecha_termino': suscripcion.fecha_termino,
                    'tarjeta': result[1],
                    'monto': suscripcion.monto
                }
                return render(request, 'pantalla_compra.html', context)
            except Exception as e:
                print(f"Error: {e}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
                raise Http404

    
    def post(self, request: HttpRequest):
        #return render(request, 'webpay.html')
        pass
class PlanOrganizacion(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        return render(request, 'plan_organizacion.html')

    
class SolicitudOrganizacionView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        form = SolicitudOrganizacionForm()
        context = {'form': form}
        return render(request, 'plan_organizacion.html', context)
    
    def post(self, request: HttpRequest):
        # Cuando se reciba una solicitud de organización, la persona queda registrada como representante
        form = SolicitudOrganizacionForm(request.POST)
        user = User.objects.get(username=request.user)
        if form.is_valid():
            solicitud = SolicitudOrganizacion(
                nombre_organizacion=form.cleaned_data['nombre_organizacion'],
                tipo_organizacion=form.cleaned_data['tipo_organizacion'],
                pais=form.cleaned_data['pais'],
                comuna=form.cleaned_data['comuna'],
                cursos=form.cleaned_data['cursos'],
                mensaje=form.cleaned_data['mensaje'],
                usuario=user
            )
            solicitud.save()
            messages.success(request, 'Hemos recibido tu solicitud con éxito.')
            return redirect('index')
        else:
            context = {'form': form}
            messages.error(request, 'No se ha podido enviar tu solicitud. Por favor, intenta nuevamente.')
            return render(request, 'plan_organizacion.html', context)

class ElegirOrganizacionView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        form = ElegirOrganizacionForm()
        context = {'form': form}
        return render(request, 'elegir_organizacion.html', context)

    def post(self, request: HttpRequest):
        form = ElegirOrganizacionForm(request.POST)
        if form.is_valid():
            id_solicitud = form.cleaned_data['organizacion']
            messages.success(request, 'Por favor, registre la suscripción.')
            return redirect('suscribir-organizacion', id_org=id_solicitud)
        else:
            context = {'form': form}
            messages.error(request, 'No se pudo recuperar los datos de la organización. Por favor, intenta nuevamente.')
            return render(request, 'elegir_organizacion.html', context)
        
class SuscripcionOrganizacionView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest, id_org):
        datos_organizacion = SolicitudOrganizacion.objects.get(id=id_org)
        initial_data = {
            'representante': datos_organizacion.usuario,
            'cursos': datos_organizacion.cursos
        }
        form = SuscripcionOrganizacionForm(initial=initial_data)
        context = {
            'id_org': id_org,
            'form': form
        }
        return render(request, 'suscribir_organizacion.html', context)
    
    def post(self, request: HttpRequest, id_org):
        form = SuscripcionOrganizacionForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            suscripcion = Suscripcion(
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                fecha_termino=form.cleaned_data['fecha_termino'],
                monto=form.cleaned_data['monto'],
                numero_usuarios=form.cleaned_data['numero_usuarios'],
                codigo_validacion='0',
                estado_suscripcion='1'
            )
            try:
                suscripcion.save()
                # Esto lo puedo hacer SOLO porque no hay más de 1 persona registrando suscripciones
                # a la vez
                ultima_suscripcion = Suscripcion.objects.all().order_by('-id')[0]
                # id_ultima_suscripcion = ultima_suscripcion.id
                # ciclo for para registrar ambos cursos en la suscripción
                cursos = str_to_list(form.cleaned_data['cursos'])
                for curso in cursos:
                    curso_object = Curso.objects.get(pk=curso)
                    curso_suscripcion = CursosSuscripcion(
                        suscripcion=ultima_suscripcion,
                        curso=curso_object
                    )
                # registro del perfil de usuario asociado a la suscripción
                user_object = User.objects.get(username=request.user)
                perfil_object = Perfil.objects.get(user_id=user_object.id)
                perfil_suscripcion = PerfilSuscripcion(
                    suscripcion=ultima_suscripcion,
                    perfil=perfil_object
                )

                curso_suscripcion.save()
                perfil_suscripcion.save()
                messages.success(request, 'La suscripción se ha registrado con éxito.')
                return redirect('index')
            except:
                print("Algo falló.")
                context = {
                    'id_org': id_org,
                    'form': form
                    }
                
                messages.error(request, 'No se ha podido registrar la suscripción. Por favor, intenta nuevamente.')
                return render(request, 'suscribir_organizacion.html', context)

        else:
            context = {
                'id_org': id_org,
                'form': form
                }
            
            messages.error(request, 'No se ha podido registrar la suscripción. Por favor, intenta nuevamente.')
            return render(request, 'suscribir_organizacion.html', context)
