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
    
    def get (self, request, id):
        curso = Curso.objects.get(pk=id)
        capitulos = pedir_capitulos(id)
        context = {
            'curso': curso,
            'capitulos': capitulos
        }
        print(curso)
        print(capitulos)
        return render(request, 'curso.html', context)
    

class CapituloView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request: HttpRequest):
        print(request.get_full_path_info)
        if request.user.is_authenticated == True:
            return render(request, 'reproductor.html')
        else:
            return render(request, 'registration/login.html')
        
    def post(self, request: HttpRequest):
        print(request.POST)