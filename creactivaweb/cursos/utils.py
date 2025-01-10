from cursos.models import Capitulo, Curso, Visualizacion
from random import shuffle
from django.db.models import Max

def pedir_capitulos(id_curso):
    return Capitulo.objects.filter(curso=id_curso)

def pedir_cursos():
    return Curso.objects.all()

def capitulos_index():
    cap_lista = []
    num_lista = [1,2,3,5,6,7,8,9,11,12]
    shuffle(num_lista)
    for num in range(7):
        cap_lista.append(Capitulo.objects.get(pk=num_lista[num]))
    return cap_lista

def pedir_ultima_visualizacion(perfil, cap):
    visualizacion = Visualizacion.objects.filter(perfil=perfil, capitulo=cap).order_by('-fecha').values()
    return visualizacion[0]['minuto']
    