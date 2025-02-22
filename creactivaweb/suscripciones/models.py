from django.db import models
from django.utils.timezone import now
from suscripciones.utils import get_tipo_organizacion
from main.models import User, Perfil
import datetime


class CodigoPromocional(models.Model):
    codigo = models.CharField(max_length=50, null=False, blank=False, verbose_name='Código promocional')
    cantidad = models.IntegerField(null=False, blank=False, verbose_name='Cantidad')
    fecha_creacion = models.DateTimeField(null=False, default=now, verbose_name='Fecha creación')
    fecha_caducidad = models.DateTimeField(null=True, blank=True, verbose_name='Fecha caducidad')
    estado_codigo = models.CharField(max_length=1, null=False, default='1', verbose_name='Estado código')

class PerfilCodigo(models.Model):
    id = models.AutoField(primary_key=True, null=False, verbose_name='ID códigos perfiles')
    codigo = models.ForeignKey(
        'CodigoPromocional',
        on_delete=models.CASCADE,
        verbose_name='ID Código Promocional'
    )
    perfil = models.ForeignKey(
        'main.Perfil',
        on_delete=models.CASCADE,
        verbose_name='ID Perfil'
    )
    estado_uso_codigo = models.CharField(max_length=1, null=False, default='0', verbose_name='Estado uso código')

class Planes(models.Model):
    nombre = models.CharField(max_length=50, null=True, verbose_name='Nombre plan')
    #tipo = models.CharField(max_field=50, default='0', verbose_name='Tipo plan')
    monto = models.IntegerField(null=True, verbose_name='Monto')
    duracion = models.IntegerField(null=True, verbose_name='Duración')
    plan_descuento = models.BooleanField(default=False, verbose_name='Es plan descuento')
    descripcion = models.CharField(max_length=255, null=True, blank=True, verbose_name='Descripción plan')

    def __str__(self):
        return f'{self.nombre} | Descuento Creactiva {self.plan_descuento}'

class Suscripcion(models.Model):
    id = models.AutoField(primary_key=True, null=False, verbose_name='ID suscripción')
    # No siempre será la fecha de ahora, solo para los usuarios individuales
    fecha_inicio = models.DateTimeField(null=False, default=now, verbose_name='Fecha inicio')
    fecha_termino = models.DateTimeField(null=True, default=now, verbose_name='Fecha término')
    monto = models.IntegerField(null=True, blank=True, default=0, verbose_name='Monto')
    numero_usuarios = models.IntegerField(null=False, default=1, verbose_name='Número usuarios')
    codigo_promocional = models.CharField(max_length=50, null=True, blank=True, default='0', verbose_name='Código promocional')
    token_ws = models.CharField(max_length=255, null=True, verbose_name='Token Webpay Service')
    tarjeta = models.CharField(max_length=10, null=True, verbose_name='Tarjeta Pago')
    fecha_transbank = models.CharField(max_length=100, null=True, verbose_name='Fecha Transbank')
    estado_transbank = models.CharField(max_length=100, null=True, verbose_name='Estado Transbank')
    session_id_transbank = models.CharField(max_length=61, null=True, blank=True, verbose_name='Session ID Transbank')
    plan = models.ForeignKey(
        Planes,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Plan',
        related_name='plan'
    )

    def __str__(self):
        return f'ID: {self.id} | Fecha término: {datetime.date.strftime(self.fecha_termino, "%d/%m/%Y")} | Plan: {self.plan.nombre}'

class CursosSuscripcion(models.Model):
    id = models.AutoField(primary_key=True, null=False,verbose_name='ID cursos suscripciones')
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
    id = models.AutoField(primary_key=True, null=False, verbose_name='ID suscripciones perfiles')
    suscripcion = models.ForeignKey(
        'Suscripcion',
        on_delete=models.CASCADE,
        verbose_name='ID Suscripción',
        related_name='suscripcion_det_per'
    )
    perfil = models.ForeignKey(
        'main.Perfil',
        on_delete=models.CASCADE,
        verbose_name='ID Perfil',
        related_name='perfil_sus'
    )
    codigo_promocional = models.ForeignKey(
        'CodigoPromocional',
        default='0',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='ID Código Promocional'
    )
    estado_suscripcion = models.CharField(max_length=1, null=False, default='0', verbose_name='Estado suscripción')
    boleta_entregada = models.BooleanField(default=False, null=True, blank=True, verbose_name='Boleta Entregada')

    def __str__(self) -> str:
        return f"Usuario: {self.perfil.user} | ID suscripción: {self.suscripcion.id} | Descuento: {self.perfil.descuento_creactiva} | Estado suscripción: {self.estado_suscripcion}"

class SolicitudOrganizacion(models.Model):
    TIPOS_ORGANIZACIONES = get_tipo_organizacion()

    nombre_organizacion = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nombre organización')
    tipo_organizacion = models.CharField(max_length=33, choices=TIPOS_ORGANIZACIONES, default=None, verbose_name='Tipo organización')
    pais = models.CharField(max_length=2, default=None, verbose_name='País')
    comuna = models.CharField(max_length=5, default=None, blank=True, verbose_name='Comuna')
    cursos = models.JSONField(null=False, blank=True, default=None, verbose_name='Cursos')
    mensaje = models.TextField(null=True, blank=True, verbose_name='Mensaje')
    usuario = models.ForeignKey(
        User,
        default=None,
        on_delete=models.CASCADE,
        verbose_name='Solicitud organización',
        related_name='solicitud_org'
    )