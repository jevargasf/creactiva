from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.utils import IntegrityError
from main.utils import *
from cursos.utils import pedir_cursos, capitulos_index
from main.forms import ContactoModelForm, SolicitarResetPasswordForm, ResetPasswordForm
from smtplib import SMTPException
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import datetime
from django.contrib.auth.hashers import make_password
from django.urls import reverse

class IndexView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request: HttpRequest):
        cursos = pedir_cursos()
        result = capitulos_index()
        capitulos = result[0]
        capitulos_lengua = result[1]
        capitulos_cultura = result[2]
        current_user = request.user
        context = {
            'cursos': cursos,
            'capitulos': capitulos,
            'capitulos_lengua': capitulos_lengua,
            'capitulos_cultura': capitulos_cultura,
            'user': current_user
        }
        return render(request, 'main/index.html', context)
    
class RegisterView(View):
    next_page = reverse_lazy('index')
    def dispatch(self, request: HttpRequest, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request: HttpRequest):
        username = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        password_repeat = request.POST['password2']
        if password != password_repeat:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'registration/register.html')
        try:
            crear_usuario(username, first_name, last_name, email, password)
            if "@creactivaanimaciones.cl" in username:
                usuario_creactiva = crear_usuario_creactiva(username)
                if usuario_creactiva == True:
                    messages.success(request, f'El usuario CreActiva fue registrado exitosamente.')
                    return redirect('index')
                else:
                    messages.error(request, 'No se pudo registrar el usuario CreActiva. Por favor, intenta nuevamente.')
                    return render(request, 'registration/register.html')
        except IntegrityError:
            messages.error(request, 'El correo ya existe')
            return render(request, 'registration/register.html')
        except Exception as e:
            messages.error(request, 'No se ha podido registrar el usuario')
            return render(request, 'registration/register.html')
        else:
            try:
                # Crear token
                user_object = User.objects.get(username=username)
                if user_object.is_active == False:
                    token = crear_token(id=user_object.id, email=user_object.email)
                    # Crear url
                    url = f'{settings.BASE_URL}accounts/verificacion/{token}'
                    correo = enviar_correo(
                        r_nombre=user_object.first_name,
                        r_email=user_object.email,
                        e_mail="no-reply@creactivaanimaciones.cl",
                        asunto="Verifica tu correo en CreActiva Animaciones",
                        app="main",
                        archivo="verify_mail",
                        url=url
                    )
                    if correo == True:
                        messages.success(request, f'La cuenta fue registrada exitosamente. Te hemos enviado un correo a {user_object.email} con un enlace para activar tu cuenta.')
                        return redirect('index')
                    else:
                        messages.error(request, f'La cuenta fue registrada exitosamente, pero no pudimos enviarte un correo para verificar tu cuenta. Por favor, escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                        return redirect('login')
            except Exception as e:
                print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
                messages.error(request, f'La cuenta fue registrada exitosamente, ocurrió un error inesperado. Por favor, escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                return redirect('login')
        
    def get(self, request):
        return render(request, 'registration/register.html')

class VerificacionView(View):
    def dispatch(self, request: HttpRequest, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request: HttpRequest, token):
        token = traducir_token(token)
        user_object = User.objects.get(pk=token['id'])
        fecha_vigencia = timezone.now() + datetime.timedelta(days=1)
        fecha_timestamp = parse_datetime(token['ts'])
        if fecha_vigencia > fecha_timestamp:
            try:
                user_object.is_active = True
                user_object.save()
                correo = enviar_correo(
                    r_nombre=user_object.first_name,
                    r_email=user_object.email,
                    e_mail="no-reply@creactivaanimaciones.cl",
                    asunto="Has creado tu cuenta en Creactiva Animaciones",
                    app="main",
                    archivo="registration_complete"
                )
                if correo == True:
                    messages.success(request, f'Hemos verificado tu cuenta exitosamente.')
                    return redirect('index')
                else:
                    messages.error(request, f'La cuenta fue verificada exitosamente, pero falló el envío del correo de éxito. Por favor, escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                    return redirect('index')
            except Exception as e:
                print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
                messages.error(request, f'Hemos verificado tu cuenta exitosamente, pero ocurrió un error inesperado. Por favor, escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                return redirect('index')
        else:
            try:
                token = crear_token(id=user_object.id, email=user_object.email)
                url = f'{settings.BASE_URL}accounts/verificacion/{token}'
                correo = enviar_correo(
                    r_nombre=user_object.first_name,
                    r_email=user_object.email,
                    e_mail="no-reply@creactivaanimaciones.cl",
                    asunto="Verifica tu correo en CreActiva Animaciones",
                    app="main",
                    archivo="verify_mail",
                    url=url
                )
                if correo == True:
                    messages.success(request, f'El token ha caducado. Te hemos enviado un nuevo enlace a {user_object.email} para activar tu cuenta.')
                    return redirect('index')
                else:
                    messages.error(request, f'El token ha caducado. Lamentablemente, no pudimos enviarte un nuevo correo para verificar tu cuenta. Por favor, escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                    return redirect('index')
            except Exception as e:
                print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
                messages.error(request, f'El token ha caducado. Lamentablemente, no pudimos enviarte un nuevo correo para verificar tu cuenta. Por favor, escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                return redirect('index')
            
class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = "Sesión Iniciada Exitosamente"
    template_name = 'registration/login.html'  
    redirect_authenticated_user = True
    


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.WARNING, "Sesión Cerrada Exitosamente")
        return response
    
class ContactoView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request: HttpRequest):
        form = ContactoModelForm()
        context = {'form': form}
        return render(request, 'main/contacto.html', context)
    
    def post(self, request: HttpRequest):
        form = ContactoModelForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            form.save()
            try:
                correo_user = enviar_correo(
                    r_nombre=nombre,
                    r_email=email,
                    e_mail="no-reply@creactivaanimaciones.cl",
                    asunto="Gracias por comunicarte con CreActiva Animaciones",
                    app="main",
                    archivo="correo_contacto"
                )
                data = {
                    'nombre': nombre,
                    'apellido': apellido,
                    'email': email,
                    'mensaje': mensaje
                }
                enviar_correo_admin(
                    r_email="contacto@creactivaanimaciones.cl",
                    e_mail="no-reply@creactivaanimaciones.cl",
                    asunto="Nuevo contacto en CreActiva Animaciones",
                    app="main",
                    archivo="notificacion_contacto_admin",
                    form=data
                )
                if correo_user == True:
                    messages.success(request, 'Hemos recibido tu mensaje con éxito.')
                    return redirect('index')
                else:
                    messages.error(request, 'Hemos recibido tu mensaje con éxito. Sin embargo, no pudimos enviarte la notificación de éxito por correo electrónico. Por favor, escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                    return redirect('index')
            except Exception as e:
                print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
                messages.error(request, 'Tu mensaje fue recibido con éxito. Sin embargo, ocurrió un error inesperado. Por favor, escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                return redirect('index')
        else:
            context = {'form': form}
            messages.error(request, 'No se ha podido enviar el mensaje. Por favor, intenta nuevamente.')
            return render(request, 'main/contacto.html', context)
        
class SugerenciasView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request: HttpRequest):
        form = ContactoModelForm()
        context = {'form': form}
        return render(request, 'main/sugerencias.html', context)
    
    def post(self, request: HttpRequest):
        form = ContactoModelForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            form.save()
            try:
                correo_user = enviar_correo(
                    r_nombre=nombre,
                    r_email=email,
                    e_mail="no-reply@creactivaanimaciones.cl",
                    asunto="Gracias por ayudarnos a mejorar",
                    app="main",
                    archivo="correo_sugerencias"
                )
                data = {
                    'nombre': nombre,
                    'apellido': apellido,
                    'email': email,
                    'mensaje': mensaje
                }
                enviar_correo_admin(
                    r_email="contacto@creactivaanimaciones.cl",
                    e_mail="no-reply@creactivaanimaciones.cl",
                    asunto="Nueva sugerencia en CreActiva Animaciones",
                    app="main",
                    archivo="notificacion_sugerencia_admin",
                    form=data
                )
                if correo_user == True:
                    messages.success(request, 'Hemos recibido tu sugerencia con éxito. Muchas gracis por ayudarnos a mejorar.')
                    return redirect('index')
                else:
                    messages.error(request, 'Hemos recibido tu mensaje con éxito. Sin embargo, no pudimos enviarte la notificación de éxito por correo electrónico. Por favor, escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                    return redirect('index')
            except Exception as e:
                print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
                messages.error(request, 'Tu mensaje fue recibido con éxito. Sin embargo, ocurrió un error inesperado. Por favor, escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                return redirect('index')
        else:
            context = {'form': form}
            messages.error(request, 'No se ha podido enviar el mensaje. Por favor, intenta nuevamente.')
            return render(request, 'main/sugerencias.html', context)
        

class NosotrosView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request: HttpRequest):
        context = {

        }
        return render(request, 'main/nosotros.html', context)
    
class ResetPasswordView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request: HttpRequest):
        form = SolicitarResetPasswordForm()
        return render(request, 'registration/password_reset.html', {'form': form})
    
    def post(self, request: HttpRequest):
        form = SolicitarResetPasswordForm(request.POST)
        email = request.POST['email']
        user_object = User.objects.get(email=email)
        if user_object is not None:
            try:
                # crear token
                token = crear_token(id=user_object.id, user=user_object.username)
                url = f'{settings.BASE_URL}accounts/password-form/{token}'
                correo = enviar_correo(
                    r_nombre=user_object.first_name,
                    r_email=user_object.email,
                    e_mail="no-reply@creactivaanimaciones.cl",
                    asunto="Reestablece tu contraseña en CreActiva Animaciones",
                    app="main",
                    archivo="reset_password",
                    url=url
                )
                if correo == True:
                    messages.success(request, f'Te hemos enviado un link para reestablecer tu contraseña a {email}.')
                    return redirect('index')
                else:
                    messages.error(request, f'No pudimos enviarte un link para reestablecer tu contraseña. Por favor, escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                    return redirect('contacto')
            except Exception as e:
                print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
                messages.error(request, f'Ocurrió un error inesperado al intentar reestablecer tu contraseña. Por favor, escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                return redirect('contacto')
        else:
            form = SolicitarResetPasswordForm()
            messages.error(request, 'El correo no existe. Por favor, intenta nuevamente.')
            return render(request, 'registration/password_reset.html', {'form': form})

class ResetPasswordConfirmView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request: HttpRequest, token):
        try:
            # recibir url con token, validar token
            token = traducir_token(token)
            user_object = User.objects.get(pk=token['id'])
            fecha_vigencia = timezone.now() + datetime.timedelta(days=1)
            fecha_timestamp = parse_datetime(token['ts'])
            if fecha_vigencia > fecha_timestamp:
                # mandar form con campos nueva contraseña
                form = ResetPasswordForm()
                context = {
                    'form': form
                }
                return render(request, 'registration/password_reset_form.html', context)
            else:
                messages.error(request, 'El token ha caducado. Por favor, intenta nuevamente.')
                return redirect('login')
        except User.DoesNotExist as e:
            print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
            messages.error(request, 'El token no es válido. Por favor, intenta nuevamente.')
            return redirect('login')


    def post(self, request: HttpRequest, token):
        form = ResetPasswordForm(request.POST)
        token = traducir_token(token)
        user_object = User.objects.get(pk=token['id'])
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                form = ResetPasswordForm()
                context = {
                    'form': form
                }
                messages.error(request, 'Las contraseñas no coinciden. Por favor, intenta nuevamente.')
                return render(request, 'registration/password_reset_form.html', context)
            else:
                try:
                    user_object.password = make_password(password1)
                    user_object.save()
                    correo = enviar_correo(
                        r_nombre=user_object.first_name,
                        r_email=user_object.email,
                        e_mail="no-reply@creactivaanimaciones.cl",
                        asunto="Contraseña restablecida exitosamente en Creactiva Animaciones",
                        app="main",
                        archivo="reset_password_done",
                    )
                    if correo == True:
                        messages.success(request, 'La contraseña se ha reestablecido satisfactoriamente. Por favor, inicia sesión.')
                        return redirect('login')
                    else:
                        messages.error(request, f'Ocurrió un error y no pudimos confirmar tu nueva contraseña. Por favor, intenta nuevamente o escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                        return redirect('login')
                except Exception as e:
                    print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
                    messages.error(request, f'Ocurrió un error y no pudimos reestablecer tu contraseña. Por favor, intenta nuevamente o escribe a contacto@creactivaanimaciones.cl para reportar este problema.')
                    return redirect('login')
        else:
            form = ResetPasswordForm()
            context = {
                'form': form
            }
            messages.error(request, 'El formulario no es válido. Por favor, intenta nuevamente.')
            return render(request, 'registration/password_reset_form.html', context)