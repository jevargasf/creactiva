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
        print(request.META.get("HTTP_REFERER"))
        curso = Curso.objects.get(pk=id)
        capitulos = pedir_capitulos(id)
        duracion_curso = 0
        actividades = 0
        num_materiales = 0
        for capitulo in capitulos:
            duracion_curso += capitulo.duracion
            actividades += capitulo.num_actividades
            if capitulo.material == None:
                continue
            else:
                num_materiales += 1
        context = {
            'curso': curso,
            'duracion': round(duracion_curso/60),
            'actividades': actividades,
            'num_materiales': num_materiales,
            'capitulos': capitulos
        }
        return render(request, 'curso.html', context)
    

class CapituloView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request: HttpRequest, id):
        print(request.META.get("HTTP_REFERER"))
        capitulo = Capitulo.objects.get(pk=id)
        context = {
            'capitulo': capitulo
        }
        if request.user.is_authenticated == True:
            return render(request, 'reproductor.html', context)
        else:
            return render(request, 'registration/login.html')
        
    def post(self, request: HttpRequest):
        print(request.POST)