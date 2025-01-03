from django.shortcuts import render
from django.views import View
from django.http import HttpRequest
from django.templatetags.static import static
from cursos.models import Curso, Capitulo
from cursos.utils import *

# Create your views here.
class CursoView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request):
        curso = Curso.objects.get(pk=1)
        capitulos = pedir_capitulos(1)
        context = {
            'curso': curso,
            'capitulos': capitulos
        }
        return render(request, 'curso.html', context)
    

class CapituloView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request: HttpRequest):
        if request.user.is_authenticated == True:
            return render(request, 'reproductor.html')
        else:
            return render(request, 'registration/login.html')
        
    def post(self, request: HttpRequest):
        print(request.POST)