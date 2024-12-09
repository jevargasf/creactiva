from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib import messages, para cuando queramos implementar alertas de error
from django.db.utils import IntegrityError
from main.utils import crear_usuario

class IndexView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request):
        return render(request, 'index.html')
    
class RegisterView(View):
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
            #messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'registration/register.html')
        try:
            crear_usuario(username, first_name, last_name, email, password)
        except IntegrityError:
            #messages.error(request, 'El correo ya existe')
            return render(request, 'registration/register.html')
        except Exception:
            #messages.error(request, 'No se ha podido registrar el usuario')
            return render(request, 'registration/register.html')
        #messages.success(request, 'Usuario creado exitosamente')
        return redirect('login')
    
    def get(self, request):
        return render(request, 'registration/register.html')
    
class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = "Sesión Iniciada Exitosamente"
    template_name = 'registration/login.html'  
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        #messages.add_message(request, messages.WARNING, "Sesión Cerrada Exitosamente")
        return response
    
class ContactoView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get (self, request):
        return render(request, 'contacto.html')