from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest
from suscripciones.forms import SolicitudOrganizacionForm, SuscripcionOrganizacionForm, ElegirOrganizacionForm
from suscripciones.models import SolicitudOrganizacion
from django.contrib import messages
from main.models import User

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
        return render(request, 'plan_individual.html')

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
            messages.success(request, 'Por favor, registre la suscripción.')

        # EL TRABAJO ACÁ ES ENVIAR EL FORMULARIO PRELLENADO
            id_solicitud = form.cleaned_data['organizacion']
            datos_organizacion = SolicitudOrganizacion.objects.get(id=id_solicitud)
            new_form = SuscripcionOrganizacionForm()
            new_form.titular = datos_organizacion.usuario
            new_form.cursos = datos_organizacion.cursos
            context = {'form': new_form}
            return render(request, 'suscribir_organizacion.html', context)
        else:
            context = {'form': form}
            messages.error(request, 'No se pudo recuperar los datos de la organización. Por favor, intenta nuevamente.')
            return render(request, 'elegir_organizacion.html', context)
        
class SuscripcionOrganizacionView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        form = SuscripcionOrganizacionForm()
        context = {'form': form}
        return render(request, 'suscribir_organizacion.html', context)
    
    def post(self, request: HttpRequest):
        form = SuscripcionOrganizacionForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'La suscripción se ha registrado con éxito.')
            return redirect('index')
        else:
            context = {'form': form}
            messages.error(request, 'No se ha podido registrar la suscripción. Por favor, intenta nuevamente.')
            return render(request, 'suscribir_organizacion.html', context)
