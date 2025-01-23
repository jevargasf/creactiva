from django.urls import path, re_path
from cursos.views import CursoView, CapituloView

urlpatterns = [
    path('cursos/<id>', CursoView.as_view(), name='cursos'),
    path('capitulo/<id>', CapituloView.as_view(), name='capitulo'),
#    re_path(r'^c1e1_player\.html\?embedIFrameId=embeddedSmartPlayerInstance', SmartPlayer.as_view(), name='player')
]
# <int:id_curso>/<str:embedIFrameId>
# POSIBLE SOLUCIóN: cursos/<id_curso>/capitulos/<id_cap>