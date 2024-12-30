from django.urls import path
from main.views import IndexView, RegisterView, CustomLoginView, CustomLogoutView, ContactoView
from django.urls import reverse_lazy

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/registro', RegisterView.as_view(next_page=''), name='register'),
    path('accounts/login', CustomLoginView.as_view(next_page=''), name='login'),
    path('accounts/logout', CustomLogoutView.as_view(next_page=''), name='logout'),
    path('contacto', ContactoView.as_view(), name='contacto')
]
#reverse_lazy('index')