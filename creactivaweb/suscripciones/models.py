from django.db import models
from django.utils.timezone import now
from suscripciones.utils import get_tipo_organizacion
from main.models import User, Perfil

class Suscripcion(models.Model):
    sus = models.AutoField(primary_key=True, null=False, verbose_name='ID suscripción')
    # No siempre será la fecha de ahora, solo para los usuarios individuales
    fecha_inicio = models.DateTimeField(null=False, default=now, verbose_name='Fecha inicio')
    fecha_termino = models.DateTimeField(null=True, verbose_name='Fecha término')
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
    TIPOS_ORGANIZACIONES = get_tipo_organizacion()

    nombre_organizacion = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nombre organización')
    tipo_organizacion = models.CharField(max_length=33, choices=TIPOS_ORGANIZACIONES, default=None, verbose_name='Tipo organización')
    pais = models.CharField(max_length=2, default=None, verbose_name='País')
    comuna = models.CharField(max_length=5, default=None, verbose_name='Comuna')
    cursos = models.JSONField(null=False, blank=True, default=None, verbose_name='Cursos')
    mensaje = models.TextField(null=True, blank=True, verbose_name='Mensaje')
    usuario = models.ForeignKey(
        User,
        default=None,
        on_delete=models.CASCADE,
        verbose_name='Solicitud organización',
        related_name='solicitud_org'
    )