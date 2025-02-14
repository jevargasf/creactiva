from cursos.models import Capitulo, Curso, Visualizacion
from main.models import Perfil
from random import shuffle
from django.db.models import Max

def pedir_capitulos(id_curso):
    return Capitulo.objects.filter(curso=id_curso)

def pedir_cursos():
    return Curso.objects.all()

def pedir_nombres_cursos():
    lista = list(Curso.objects.all().values('cur', 'nombre'))
    nombres = []
    for dic in lista:
        nombres.append([str(dic['cur']), dic['nombre']])
    return nombres

def data_curso(id_curso):
    curso = Curso.objects.get(pk=id_curso)
    capitulos = pedir_capitulos(id_curso)
    duracion_curso = 0
    actividades = 0
    num_materiales = 0
    for capitulo in capitulos:
        duracion_curso += capitulo.duracion
        actividades += capitulo.num_actividades
        if capitulo.material == None:
            continue
        else:
            num_materiales += 1
    context = {
        'curso': curso,
        'duracion': round(duracion_curso/60),
        'actividades': actividades,
        'num_materiales': num_materiales,
        'capitulos': capitulos
    }
    return context

def capitulos_index():
    caps = Capitulo.objects.all()
    cap_lista = []
    num_lista = [1,2,3,5,6,7,8,9,11,12]
    shuffle(num_lista)
    for num in range(7):
        for cap in caps:
            if cap.cap == num_lista[num]:
                cap_lista.append(cap)

    caps_lengua = []
    caps_cultura = []
    for cap in caps:
        if cap.curso.cur == 1:
            caps_lengua.append(cap)
        else:
            caps_cultura.append(cap)
    return [cap_lista, caps_lengua, caps_cultura]

def pedir_ultima_visualizacion(perfil, cap):
    visualizacion = Visualizacion.objects.filter(perfil=perfil, capitulo=cap).order_by('-fecha').values()
    
    if len(visualizacion) != 0:
        return visualizacion[0]['minuto']
    else:
        return None

def pedir_perfil(username):
    return Perfil.objects.get(user=username)