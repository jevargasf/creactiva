from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest
from suscripciones.forms import SolicitudOrganizacionForm, SuscripcionOrganizacionForm, ElegirOrganizacionForm
from suscripciones.models import SolicitudOrganizacion, Suscripcion, CursosSuscripcion, PerfilSuscripcion, Planes
from suscripciones.utils import str_to_list
from django.contrib import messages
from main.models import User, Perfil
from cursos.models import Curso

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
    
class PlanOrganizacion(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        return render(request, 'plan_organizacion.html')

class PagarView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        return render(request, 'pantalla_compra.html')
    
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
                print(type(cursos))
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
                print(perfil_suscripcion)

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
