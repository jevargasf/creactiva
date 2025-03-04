from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.utils import IntegrityError
from main.utils import crear_usuario, crear_token, traducir_token
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
                token = crear_token(id=user_object.id, email=user_object.email)
                # Crear url
                url = f'{settings.BASE_URL}accounts/verificacion/{token}'
                # Preparar html
                text_content = render_to_string(
                    "templates/mails/verify_mail.txt",
                    context={
                        'nombre': user_object.first_name,
                        'url': url
                    }
                )
                html_content = render_to_string(
                    'templates/mails/verify_mail.html',
                    context={
                        'nombre': user_object.first_name,
                        'url': url
                    }
                )
                # Enviar por email
                msg = EmailMultiAlternatives(
                    "Verifica tu correo en Creactiva Animaciones",
                    text_content,
                    "no-reply@creactivaanimaciones.cl",
                    [user_object.email]
                )
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                # Retornar mensaje
                messages.success(request, f'La cuenta fue registrada exitosamente. Te hemos enviado un correo a {email} con un enlace para activar tu cuenta.')
                return redirect('index')
            except SMTPException as e:
                print("NO SE PUDO ENVIAR EL CORREO.", e)
                messages.error(request, f'La cuenta fue registrada exitosamente, pero no pudimos enviarte un correo para verificar tu cuenta. Por favor, escribe a contacto@creactivaanimaciones.cl para solucionar este problema.')
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
            user_object.is_active = True
            user_object.save()
            messages.success(request, f'Hemos verificado tu cuenta exitosamente.')
            return redirect('index')
        else:
            try:
                token = crear_token(id=user_object.id, email=user_object.email)
                url = f'{settings.BASE_URL}accounts/verificacion/{token}'
                text_content = render_to_string(
                    "templates/mails/verify_mail.txt",
                    context={
                        'nombre': user_object.first_name,
                        'url': url
                    }
                )
                html_content = render_to_string(
                    'templates/mails/verify_mail.html',
                    context={
                        'nombre': user_object.first_name,
                        'url': url
                    }
                )
                msg = EmailMultiAlternatives(
                    "Verifica tu correo en Creactiva Animaciones",
                    text_content,
                    "no-reply@creactivaanimaciones.cl",
                    [user_object.email]
                )
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                messages.success(request, f'El token ha caducado. Te hemos enviado un nuevo enlace a {user_object.email} para activar tu cuenta.')
                return redirect('index')
            except SMTPException as e:
                print("NO SE PUDO ENVIAR EL CORREO.", e)
                messages.error(request, f'La cuenta fue registrada exitosamente, pero no pudimos enviarte un correo para verificar tu cuenta. Por favor, escribe a contacto@creactivaanimaciones.cl para solucionar este problema.')
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
            form.save()
            try:
                text_content = render_to_string(
                    "templates/mails/correo_contacto.txt",
                    context={
                        'nombre': f'{nombre} {apellido}',
                    }
                )
                html_content = render_to_string(
                    'templates/mails/correo_contacto.html',
                    context={
                        'nombre': f'{nombre} {apellido}',
                    }
                )
                msg = EmailMultiAlternatives(
                    "Gracias por comunicarte con Creactiva Animaciones",
                    text_content,
                    "no-reply@creactivaanimaciones.cl",
                    [email]
                )
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                messages.success(request, 'Hemos recibido tu mensaje con éxito.')
                return redirect('index')
            except SMTPException as e:
                messages.success(request, 'Hemos recibido tu mensaje con éxito.')
                print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
                return redirect('index')
            except Exception as e:
                messages.success(request, 'Hemos recibido tu mensaje con éxito.')
                print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
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
            form.save()
            try:
                text_content = render_to_string(
                    "templates/mails/correo_sugerencias.txt",
                    context={
                        'nombre': f'{nombre} {apellido}',
                    }
                )
                html_content = render_to_string(
                    'templates/mails/correo_sugerencias.html',
                    context={
                        'nombre': f'{nombre} {apellido}',
                    }
                )
                msg = EmailMultiAlternatives(
                    "Gracias por ayudarnos a mejorar",
                    text_content,
                    "no-reply@creactivaanimaciones.cl",
                    [email]
                )
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                messages.success(request, 'Hemos recibido tu mensaje con éxito.')
                return redirect('index')
            except SMTPException as e:
                messages.success(request, 'Hemos recibido tu mensaje con éxito.')
                print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
                return redirect('index')
            except Exception as e:
                messages.success(request, 'Hemos recibido tu mensaje con éxito.')
                print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
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
        if form.is_valid():
            email = request.POST['email']
            # crear token
            print(email)
            user_object = User.objects.get(email=email)
            token = crear_token(id=user_object.id, user=user_object.username)
            url = f'{settings.BASE_URL}accounts/password-form/{token}'
            text_content = render_to_string(
                "templates/mails/reset_password.txt",
                context={
                    'nombre': user_object.first_name,
                    'url': url
                }
            )
            html_content = render_to_string(
                'templates/mails/reset_password.html',
                context={
                    'nombre': user_object.first_name,
                    'url': url
                }
            )
            msg = EmailMultiAlternatives(
                "Reestablece tu contraseña en Creactiva Animaciones",
                text_content,
                "no-reply@creactivaanimaciones.cl",
                [user_object.email]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            # mandar correo con token
            messages.success(request, f'Te hemos enviado un link para reestablecer tu contraseña a {email}.')
            return redirect('index')
        else:
            form = SolicitarResetPasswordForm()
            messages.error(request, 'No se ha podido reestablecer la contraseña. Por favor, intenta nuevamente.')
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
                    text_content = render_to_string(
                        "templates/mails/reset_password_done.txt",
                        context={
                            'nombre': user_object.first_name,
                        }
                    )
                    html_content = render_to_string(
                        'templates/mails/reset_password_done.html',
                        context={
                            'nombre': user_object.first_name,
                        }
                    )
                    msg = EmailMultiAlternatives(
                        "Contraseña Restablecida Exitosamente Creactiva Animaciones",
                        text_content,
                        "no-reply@creactivaanimaciones.cl",
                        [user_object.email]
                    )
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                    messages.success(request, 'La contraseña se ha reestablecido satisfactoriamente. Por favor, inicie sesión.')
                    return redirect('login')
                except SMTPException as e:
                    messages.error(request, f'Ocurrió un error. No pudimos confirmar tu nueva contraseña. Por favor, intenta nuevamente')
                    return redirect('login')
                except Exception as e:
                    messages.error(request, f'Ocurrió un error. No pudimos reestablecer tu contraseña. Por favor, intenta nuevamente')
                    return redirect('login')
        else:
            form = ResetPasswordForm()
            context = {
                'form': form
            }
            messages.error(request, 'El formulario no es válido. Por favor, intenta nuevamente.')
            return render(request, 'registration/password_reset_form.html', context)