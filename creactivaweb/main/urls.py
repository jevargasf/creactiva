from django.urls import path
from main.views import *
from django.urls import reverse_lazy

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/registro', RegisterView.as_view(next_page=''), name='register'),
    path('accounts/verificacion/<str:token>', VerificacionView.as_view(), name='verify'),
    path('accounts/reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('accounts/password-form/<token>', ResetPasswordConfirmView.as_view(), name='password-form'),
    path('accounts/login', CustomLoginView.as_view(next_page=''), name='login'),
    path('accounts/logout', CustomLogoutView.as_view(next_page=''), name='logout'),
    path('contacto', ContactoView.as_view(), name='contacto'),
    path('nosotros', NosotrosView.as_view(), name='nosotros')
]
