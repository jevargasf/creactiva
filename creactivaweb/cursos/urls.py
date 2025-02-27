from django.urls import path, re_path
from cursos.views import *

urlpatterns = [
    path('cursos', CursosPrincipalView.as_view(), name='cursos-principal'),
    path('curso/<id>', CursoView.as_view(), name='curso'),
    # path('trailer/<id>', TrailerView.as_view(), name='trailer'),
    path('capitulo/<id>', CapituloView.as_view(), name='capitulo'),
    path('recursos/glosario', RecursosView.as_view(), name='recursos'),

]
# <int:id_curso>/<str:embedIFrameId>
# POSIBLE SOLUCIóN: cursos/<id_curso>/capitulos/<id_cap>