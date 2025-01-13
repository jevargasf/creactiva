from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.templatetags.static import static
from cursos.models import Curso, Capitulo, Visualizacion, EstadoCapitulo
from cursos.utils import *
from main.models import User, Perfil
from django.utils import timezone

class CursoView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request, id):
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
        perfil = Perfil.objects.get(user=request.user)
        
        capitulo = Capitulo.objects.get(pk=id)
        #ultima_visualizacion = pedir_ultima_visualizacion(perfil, capitulo)
        
        #ult_visualizacion = Visualizacion.objects.get(fecha=fecha_ult_visualizacion)
        # enviar en el context el último segundo de reproducción al navegador
        # identificarlo a través del usuario, el capítulo y el último segundo
        
        context = {
            'capitulo': capitulo,
            #'minuto': ultima_visualizacion
        }
        if request.user.is_authenticated == True:
            return render(request, 'reproductor.html', context)
        else:
            return render(request, 'registration/login.html', context)
        
    def post(self, request: HttpRequest, id):
        # código para almacenar el segundo de reproducción
        # ver bien el evento que desencadenará la escritura de la bbdd
        # el document.visibility hidden puede que envíe demasidas peticiones
        # pero el unload o el beforeunload tienen más casos de fallo
        res = request.body
        t_string = res.decode('utf-8').replace('"','')
        t_float = float(t_string)
        capitulo = Capitulo.objects.get(cap=id)
        # if t_reproduccion != null, almacenar, si no, continuar
        # guardo el correo, porque con eso puedo recuperar el código perfil y demás información
        # de cliente
        perfil = Perfil.objects.get(user=request.user)
        visualizacion = Visualizacion(
            perfil=perfil,
            capitulo=capitulo,
            minuto=t_float,
            fecha=timezone.now()
        )
        visualizacion.save()
        # GUARDAR UNA VISUALIZACIÓN
        # necesito: perfil del usuario, cap (que sale del id recibido en request),
        # el minuto recuperado y la fecha es autoadd
        return HttpResponse(status = 200)