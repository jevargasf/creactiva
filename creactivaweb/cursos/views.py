from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.templatetags.static import static
from cursos.models import *
from cursos.utils import *
from main.models import User, Perfil
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import json


class CursosPrincipalView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request):
        cursos = pedir_cursos()
        result = capitulos_index()
        capitulos = result[0]
        capitulos_lengua = result[1]
        capitulos_cultura = result[2]
        context = {
            'cursos': cursos,
            'capitulos': capitulos,
            'capitulos_lengua': capitulos_lengua,
            'capitulos_cultura': capitulos_cultura
        }
        return render(request, 'cursos/cursos_principal.html', context)

class CursoView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request, id):
        context = data_curso(id)
        return render(request, 'cursos/curso.html', context)
    
class TrailerView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request: HttpRequest, id): 
        context = data_curso(id)
        return render(request, 'cursos/trailer.html', context)

class CapituloView(View):
    # TIENE QUE LLEGAR DESDE UN BOTÓN EN EL TEMPLATE TRAILER
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get (self, request: HttpRequest, id):
        capitulo = Capitulo.objects.get(pk=id)
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
                'contenidos': capitulo.contenidos,
                'first_frame': capitulo.first_frame,
                'etiqueta_promocional_id': capitulo.etiqueta_promocional,
                'etiqueta_promocional': capitulo.get_etiqueta_promocional_display(),
                'fecha_lanzamiento': capitulo.fecha_lanzamiento
            },
            'recurso': {}
        }
        if request.user.is_authenticated:
                # TIENE CUENTA      
            perfil_object = pedir_perfil(request.user)
            # TIENE SUSCRIPCIÓN INDIVIDUAL
            if perfil_object.codigo[0] == '1':
                if capitulo.etiqueta_promocional == '0':
                    context['recurso']['js_cap'] = capitulo.js_cap
                    context['recurso']['link'] = capitulo.link
                    context['recurso']['xml_cap'] = capitulo.xml_cap
                    ultima_visualizacion = pedir_ultima_visualizacion(perfil_object, capitulo)
                    if ultima_visualizacion != None:
                        context['minuto'] = ultima_visualizacion
                    
                    return render(request, 'cursos/reproductor.html', context)
                else:
                    context['recurso']['js_trailer'] = capitulo.curso.js_trailer
                    context['recurso']['xml_trailer'] = capitulo.curso.xml_trailer
                    context['recurso']['link'] = capitulo.curso.link_trailer
                    return render(request, 'cursos/trailer.html', context)

            # NO TIENE SUSCRIPCIÓN INDIVIDUAL, MANDA INFO TRAILER EN VEZ DE MANDAR CONTEXT, MEJO REDIRECT A URL TRAILER
            else:
                context['suscripcion'] = 'ninguna'
                context['recurso']['js_trailer'] = capitulo.curso.js_trailer
                context['recurso']['xml_trailer'] = capitulo.curso.xml_trailer
                context['recurso']['link'] = capitulo.curso.link_trailer
                # DATA CAP + TRAILER
                return render(request, 'cursos/trailer.html', context)
        else:
            context['recurso']['js_trailer'] = capitulo.curso.js_trailer
            context['recurso']['xml_trailer'] = capitulo.curso.xml_trailer
            context['recurso']['link'] = capitulo.curso.link_trailer
            # DATA CAP + TRAILER
            return render(request, 'cursos/trailer.html', context)
        
    def post(self, request: HttpRequest, id):
        # código para almacenar el segundo de reproducción
        # ver bien el evento que desencadenará la escritura de la bbdd
        # el document.visibility hidden puede que envíe demasidas peticiones
        # pero el unload o el beforeunload tienen más casos de fallo
        res = json.loads(request.body)
        # t_string = res['minuto'].replace('"','')
        t_float = float(res['minuto'])
        print(t_float)
        capitulo = Capitulo.objects.get(cap=id)
        # if t_reproduccion != null, almacenar, si no, continuar
        # guardo el correo, porque con eso puedo recuperar el código perfil y demás información
        # de cliente
        user_clean = res['user'].strip('"')
        print(user_clean)
        user_object = User.objects.get(username=user_clean)
        perfil = Perfil.objects.get(user=user_object)
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
    
class GlosarioView(LoginRequiredMixin, View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request: HttpRequest):
        perfil_object = pedir_perfil(request.user)
        # TIENE SUSCRIPCIÓN INDIVIDUAL
        if perfil_object.codigo[0] == '1':
            return render(request, 'cursos/recursos/glosario.html')
        else:
            messages.error(request, 'Suscríbete a uno de nuestros planes para acceder a este y otros contenidos.')
            return redirect('plan-individual')