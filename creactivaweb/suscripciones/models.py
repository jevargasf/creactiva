from django.db import models
from django.utils.timezone import now
from suscripciones.utils import get_tipo_organizacion

class Suscripcion(models.Model):
    sus = models.AutoField(primary_key=True, null=False, verbose_name='ID suscripción')
    fecha_inicio = models.DateTimeField(null=False, default=now, verbose_name='Fecha inicio')
    fehca_termino = models.DateTimeField(null=True, verbose_name='Fecha término')
    monto = models.IntegerField(null=True, verbose_name='Monto')
    numero_usuarios = models.IntegerField(null=False, default=1, verbose_name='Número usuarios')
    codigo_validacion = models.CharField(max_length=255, null=True, verbose_name='Código validación')
    estado_suscripcion = models.IntegerField(null=False, default=0, verbose_name='Estado suscripción')


class CursosSuscripcion(models.Model):
    cur_sus = models.AutoField(primary_key=True, null=False,verbose_name='ID cursos suscripciones')
    suscripcion = models.ForeignKey(
        'Suscripcion',
        on_delete=models.CASCADE,
        verbose_name='Suscripción Detalle Curso',
        related_name='suscripcion_det_cur'
    )
    curso = models.ForeignKey(
        'cursos.Curso',
        on_delete=models.CASCADE,
        verbose_name='Curso suscrito',
        related_name='curso_sus'
    )

class PerfilSuscripcion(models.Model):
    usu_sus = models.AutoField(primary_key=True, null=False, verbose_name='ID suscripciones perfiles')
    suscripcion = models.ForeignKey(
        'Suscripcion',
        on_delete=models.CASCADE,
        verbose_name='Suscripción Detalle Perfil',
        related_name='suscripcion_det_per'
    )
    perfil = models.ForeignKey(
        'main.Perfil',
        on_delete=models.CASCADE,
        verbose_name='Perfil suscripción',
        related_name='perfil_sus'
    )

class SolicitudOrganizacion(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nombre')
    apellido = models.CharField(max_length=255, null=True, blank=True, verbose_name='Apellido')
    #tipo_organizacion = models.Choices()