from cursos.models import Capitulo, Curso

def pedir_capitulos(id_curso):
    return Capitulo.objects.filter(curso=id_curso)

def pedir_cursos():
    return Curso.objects.all()