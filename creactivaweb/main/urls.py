from django.urls import path
from main.views import *
from django.urls import reverse_lazy

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/registro', RegisterView.as_view(next_page=''), name='register'),
    path('accounts/change-password', ResetPasswordView.as_view(), name='change_password'),
    path('accounts/confirm-password/<uidb64><token>', ConfirmResetPasswordView.as_view(), name='password_reset_confirm'),
    path('accounts/login', CustomLoginView.as_view(next_page=''), name='login'),
    path('accounts/logout', CustomLogoutView.as_view(next_page=''), name='logout'),
    path('contacto', ContactoView.as_view(), name='contacto'),
    path('nosotros', NosotrosView.as_view(), name='nosotros')
]
