from django.urls import path
from cursos.views import CursoView, CapituloView

urlpatterns = [
    path('cursos/', CursoView.as_view(), name='curso'),
    path('capitulo/', CapituloView.as_view(), name='capitulo')
]