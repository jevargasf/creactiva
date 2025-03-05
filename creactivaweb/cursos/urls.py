from django.urls import path, re_path
from cursos.views import *

urlpatterns = [
    path('cursos', CursosPrincipalView.as_view(), name='cursos-principal'),
    path('curso/<id>', CursoView.as_view(), name='curso'),
    # path('trailer/<id>', TrailerView.as_view(), name='trailer'),
    path('capitulo/<id>', CapituloView.as_view(), name='capitulo'),
    path('glosario', RecursosView.as_view(), name='recursos'),
]