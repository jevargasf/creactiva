from django.shortcuts import render
from django.views import View
from django.http import HttpRequest


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