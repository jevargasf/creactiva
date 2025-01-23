from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest
from suscripciones.forms import SolicitudOrganizacionForm, SuscripcionOrganizacionForm
from django.contrib import messages
from cursos.utils import pedir_nombres_cursos
from suscripciones.utils import get_representantes

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
        if form.is_valid():
            form.save()
            messages.success(request, 'Hemos recibido tu solicitud con éxito.')
            return redirect('index')
        else:
            context = {'form': form}
            messages.error(request, 'No se ha podido enviar tu solicitud. Por favor, intenta nuevamente.')
            return render(request, 'plan_organizacion.html', context)
            
class SuscripcionOrganizacionView(View):
    def dispatch(self, *args, **kwargs):
            return super().dispatch(*args, **kwargs)

    def get(self, request: HttpRequest):
        get_representantes()
        form = SuscripcionOrganizacionForm()
        context = {'form': form}
        return render(request, 'suscribir_organizacion.html', context)
    
    def post(self, request: HttpRequest):
        form = SuscripcionOrganizacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La suscripción se ha registrado con éxito.')
            return redirect('index')
        else:
            context = {'form': form}
            messages.error(request, 'No se ha podido registrar la suscripción. Por favor, intenta nuevamente.')
            return render(request, 'suscribir_organizacion.html', context)
