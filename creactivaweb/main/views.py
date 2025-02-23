from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeDoneView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.utils import IntegrityError
from main.utils import crear_usuario
from cursos.utils import pedir_cursos, capitulos_index
from main.forms import ContactoModelForm
from django.core.mail import send_mail
from smtplib import SMTPException
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm

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
        # Validación del password ingresado
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
        # método authenticate(request, **credentials)
        else:
            messages.success(request, 'Usuario creado exitosamente')
            # user = authenticate(username=username, password=password)
            # if user is not None:
            #     login(request, user)
            try:
                send_mail(
                    "Bienvenido a Creactiva Animaciones",
                    "Por favor, ingresa a esta dirección para confirmar tu dirección de correo electrónico.",
                    "no-reply@creactivaanimaciones.cl",
                    [request.POST['email']],
                    fail_silently=False,
                )
            except SMTPException as e:
                print("NO SE PUDO ENVIAR EL CORREO.", e)
            return redirect('login')
            # else:
            #     messages.error(request, 'Login inválido')
            #     return render(request, 'registration/register.html')
        
    def get(self, request):
        return render(request, 'registration/register.html')
    
class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = "Sesión Iniciada Exitosamente"
    template_name = 'registration/login.html'  
    redirect_authenticated_user = True

    # def dispatch(self, request, *args, **kwargs):
    #     response = super().dispatch(request, *args, **kwargs)
    #     storage = messages.get_messages(request)
    #     for message in storage:
    #         print(message)  # Optional: Print messages for debugging or logging purposes
    #     storage.used = True  # Mark messages as used to clear them from storage
    #     messages.error(request, "No se pudo iniciar sesión. Intente nuevamente.")
    #     messages.success(request, "Sesión iniciada exitosamente.")
    #     return response


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
            form.save()
            messages.success(request, 'Hemos recibido tu mensaje con éxito.')
            return redirect('index')
        else:
            context = {'form': form}
            messages.error(request, 'No se ha podido enviar el mensaje. Por favor, intenta nuevamente.')
            return render(request, 'main/contacto.html', context)
        
class NosotrosView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request: HttpRequest):
        context = {

        }
        return render(request, 'main/nosotros.html', context)
    
class ResetPasswordView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    from_email = 'no-reply@creactivaanimaciones.cl'
    # form_class = PasswordResetForm()
    # success_url = reverse_lazy('index')
    # template_name = 'change_password'

    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)
    
    # def get(self, request: HttpRequest):
    #     form_class = PasswordResetForm()
    #     return render(request, 'change_password.html', {'form': form_class})
    
    # def post(self, request: HttpRequest):
    #     form = PasswordResetForm(request.POST)
    #     if form.is_valid():
    #         print(form)
    #         email = form['email']
    #         form.send_mail(
    #             subject_template_name='Reestablecer Contraseña Creactiva Animaciones',
    #             email_template_name='Acá puedes reestablecer tu contraseña: ',
    #             from_email='no-reply@creactivaanimaciones.cl',
    #             to_email=email,
    #         )
    #         print(email)
    #         messages.success(request, f'Te hemos enviado un link para reestablecer tu contraseña a {email}.')
    #         return redirect('login')
    #     else:
    #         form = PasswordResetForm()
    #         messages.error(request, 'No se ha podido reestablecer la contraseña. Por favor, intenta nuevamente.')
    #         return render(request, 'registration/change_password.html', {'form': form})

class DoneResetPasswordView(PasswordChangeDoneView):
    template_name = 'registration/password_reset_done.html'

class ConfirmResetPasswordView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'

