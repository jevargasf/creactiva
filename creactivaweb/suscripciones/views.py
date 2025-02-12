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
from suscripciones.services import suscripcion_activa, suscripcion_session
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from smtplib import SMTPException

class PlanesView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        
        return render(request, 'elegir_tipo.html')

####### MANEJO DE SUSCRIPCIONES INDIVIDUALES #######
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
    
    def post(self, request: HttpRequest, id_plan):
        pass

class PagarView(LoginRequiredMixin, View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        return render(request, 'pantalla_compra.html')
    
    def post(self, request: HttpRequest, id_plan):
        try:
            check_suscripcion = suscripcion_activa(request.user)
            print(check_suscripcion)
            if check_suscripcion != None:
                context = {
                    'fecha_inicio': check_suscripcion.fecha_inicio,
                    'fecha_termino': check_suscripcion.fecha_termino,
                    'tipo': check_suscripcion.plan.nombre
                }
                return render(request, 'suscripcion_activa.html', context)
            elif check_suscripcion == None:
                plan = Planes.objects.get(pk=id_plan)
                fecha_inicio = now()
                fecha_termino = sumar_fecha(fecha_inicio, plan.duracion)
                suscripcion = Suscripcion(
                    fecha_inicio=fecha_inicio,
                    # fecha término es now + duración de la suscripción
                    fecha_termino=fecha_termino,
                    monto=plan.monto,
                    numero_usuarios=1,
                    codigo_validacion='0',
                    plan=plan
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
                    suscripcion=suscripcion,
                    estado_suscripcion='2'
                )
                perfil_suscripcion.save()
            

            # CREAR TRANSACCIÓN 
            respuesta = crear_transaccion(suscripcion.id, suscripcion.plan.monto)

            context = {
                'url': respuesta['url'],
                'token': respuesta['token']
            }

            return render(request, 'webpay.html', context)
        except User.DoesNotExist as e:
            print(f"Error: {e}")
            messages.error(request, 'Por favor, ingresa antes de continuar. Si no tienes una cuenta, regístrate.')
            return redirect('login')
        except Exception as e:
            print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
            messages.error(request, 'No se ha podido registrar la suscripción. Por favor, intenta nuevamente.')
            return redirect('plan-individual')

    
class RespuestaWebpayView(LoginRequiredMixin, View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        try:
            # RECIBIR EL RESULTADO DEL REDIRECCIONAMIENTO WEBPAY
            # CUANDO ANULO UNA TRANSACCIÓN, EL TOKEN NO VUELVE COMO TOKEN_WS, VUELVE COMO TBK_TOKEN
            if request.GET.get('TBK_TOKEN'):
                token = request.GET.get('TBK_TOKEN')
            elif request.GET.get('token_ws'):
                token = request.GET.get('token_ws')
            else:
                raise Http404
            
            # PROCESO WEBPAY
            result = confirmar_transaccion(token)

            # PROCESAR LA RESPUESTA WEBPAY
            if result[0] == 'vacio':
                raise Http404
            elif result[0] == 'AUTHORIZED':
                session_id = result[3]
                nueva_fecha_inicio = now()
                suscripcion = suscripcion_session(session_id)
                suscripcion.fecha_inicio = nueva_fecha_inicio
                suscripcion.fecha_termino = sumar_fecha(nueva_fecha_inicio, suscripcion.plan.duracion)
                suscripcion.estado_transbank=result[0]
                suscripcion.tarjeta=result[1]
                suscripcion.fecha_transbank=result[2]
                suscripcion.token_ws=token
                suscripcion.session_id_transbank = 'DESTROYED'
                suscripcion.save()
                user_object = User.objects.get(username=request.user)
                perfil_object = Perfil.objects.get(user_id=user_object.id)
                perfil_object.codigo = '100'
                perfil_object.save()
                perfil_suscripcion_object = PerfilSuscripcion.objects.get(suscripcion_id=suscripcion.id)
                perfil_suscripcion_object.estado_suscripcion = '1'
                perfil_suscripcion_object.save()
                send_mail(
                    f"Nueva Suscripción Creactiva Animaciones",
                    f"""Detalles de la suscripción: Nombre usuario: {user_object.first_name} {user_object.last_name}, 
                    Correo: {user_object.email}, Tipo suscripción: Individual, Plan: {suscripcion.plan.nombre}, 
                    Monto: {suscripcion.plan.monto}, Duración: {suscripcion.plan.duracion} meses,  
                    Fecha inicio: {suscripcion.fecha_inicio}, Fecha término: {suscripcion.fecha_termino}.""",
                    "no-reply@creactivaanimaciones.cl",
                    ["contacto@creactivaanimaciones.cl"],
                    fail_silently=False,
                )
                messages.success(request, 'Tu suscripción ha sido procesada con éxito.')
                context = {
                    'orden_compra': suscripcion.id,
                    'fecha_inicio': suscripcion.fecha_inicio,
                    'fecha_termino': suscripcion.fecha_termino,
                    'tarjeta': result[1],
                    'monto': suscripcion.monto
                }
                return render(request, 'voucher_webpay.html', context)
            elif result[0] == 'FAILED':
                session_id = result[3]
                suscripcion = suscripcion_session(session_id)
                suscripcion.estado_transbank=result[0]
                suscripcion.tarjeta=result[1]
                suscripcion.fecha_transbank=result[2]
                suscripcion.token_ws=token
                suscripcion.session_id_transbank = 'DESTROYED'
                suscripcion.save()
                messages.error(request, 'Lo sentimos, ocurrió un error. Por favor, intenta nuevamente.')
                return redirect(f'planes/individual/{suscripcion.plan.id}')
            elif result[0] == 'ABORTED':
                session_id = request.GET.get('TBK_ID_SESION')
                suscripcion = suscripcion_session(session_id)
                suscripcion.estado_transbank=result[0]
                suscripcion.tarjeta='XXXX'
                suscripcion.fecha_transbank=now()
                suscripcion.token_ws=token
                suscripcion.session_id_transbank = 'DESTROYED'
                suscripcion.save()
                messages.error(request, 'La operación fue anulada por el usuario.')
                return redirect(f'planes/individual/{suscripcion.plan.id}')
        except SMTPException as e:
            print("NO SE PUDO ENVIAR EL CORREO.", e)
        except Exception as e:
            print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
            raise Http404
    
    def post(self, request: HttpRequest):
        pass

####### MANEJO DE SUSCRIPCIONES ORGANIZACIÓN ########
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
