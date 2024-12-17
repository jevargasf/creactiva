from django.shortcuts import render
from django.views import View
from django.http import HttpRequest
from django.templatetags.static import static

# Create your views here.
class CursoView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request):
        return render(request, 'curso.html')
    

class CapituloView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request: HttpRequest):
        request.content_params = {
            'embedIFrameId': 'embeddedSmartPlayerInstance'
        }
        return render(request, 'c1e1_player.html')
    
class SmartPlayer(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get (self, request: HttpRequest):

        return render(request, 'c1e1_player.html')