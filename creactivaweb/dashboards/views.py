from django.shortcuts import render
from django.views import View
from dashboards.utils import suscripcion_activa

# Create your views here.
class PerfilIndividualView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request):
        # necesito data del perfil del usuario y de su suscripción
        context = suscripcion_activa(request.user)
        print(context)
        return render(request, 'perfiles/perfil.html', context)
    
    def post (self, request, id):
        pass