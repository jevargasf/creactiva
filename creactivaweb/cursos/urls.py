from django.urls import path, re_path
from cursos.views import CursoView, CapituloView, SmartPlayer

urlpatterns = [
    path('cursos/', CursoView.as_view(), name='curso'),
    path('capitulo/', CapituloView.as_view(), name='capitulo'),
    re_path(r'^c1e1_player\.html\?embedIFrameId=embeddedSmartPlayerInstance', SmartPlayer.as_view(), name='player')
]
# <int:id_curso>/<str:embedIFrameId>