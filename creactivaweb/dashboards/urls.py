from django.urls import path
from dashboards.views import PerfilIndividualView

urlpatterns = [
    path('perfil', PerfilIndividualView.as_view(), name='perfil'),
]