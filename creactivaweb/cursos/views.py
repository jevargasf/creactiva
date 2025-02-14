from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.templatetags.static import static
from cursos.models import Curso, Capitulo, Visualizacion, EstadoCapitulo
from cursos.utils import *
from main.models import User, Perfil
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class CursoView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request, id):
        context = data_curso(id)
        return render(request, 'curso.html', context)
    
class TrailerView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request: HttpRequest, id): 
        context = data_curso(id)
        return render(request, 'trailer.html', context)

class CapituloView(View):
    # TIENE QUE LLEGAR DESDE UN BOTÓN EN EL TEMPLATE TRAILER
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get (self, request: HttpRequest, id):
        capitulo = Capitulo.objects.get(pk=id)
        if request.user.is_authenticated:
            context = {
                'info': {
                    'capitulo_nombre': capitulo.nombre,
                    'curso_nombre': capitulo.curso.nombre,
                    'curso_id': capitulo.curso.cur,
                    'desc_corta': capitulo.desc_corta,
                    'numero': capitulo.numero,
                    'descripcion': capitulo.descripcion,
                    'duracion': capitulo.duracion,
                    'first_frame': capitulo.first_frame,
                    'contenidos': capitulo.contenidos
                },
                'recurso': {}
            }
                # TIENE CUENTA      
            perfil_object = pedir_perfil(request.user)
            # TIENE SUSCRIPCIÓN INDIVIDUAL
            if perfil_object.codigo[0] == '1':
                context['recurso']['js_cap'] = capitulo.js_cap
                context['recurso']['link'] = capitulo.link
                context['recurso']['xml_cap'] = capitulo.xml_cap
                context['recurso']['first_frame'] = capitulo.first_frame
                ultima_visualizacion = pedir_ultima_visualizacion(perfil_object, capitulo)
                if ultima_visualizacion != None:
                    context['minuto'] = ultima_visualizacion
                
                return render(request, 'reproductor.html', context)
            # NO TIENE SUSCRIPCIÓN INDIVIDUAL, MANDA INFO TRAILER EN VEZ DE MANDAR CONTEXT, MEJO REDIRECT A URL TRAILER
            else:
                context = data_curso(capitulo.curso.cur)
                return redirect('trailer', capitulo.curso.cur)
        else:
            context = data_curso(capitulo.curso.cur)
            return redirect('trailer', capitulo.curso.cur)
        
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