from django.db import models
from django.contrib.auth.models import User
from cursos.models import Capitulo
from suscripciones.utils import get_tipo_organizacion, get_paises, get_comunas


class Perfil(models.Model):
    TIPOS_ORGANIZACION = get_tipo_organizacion()
    PAISES = get_paises()
    COMUNAS = get_comunas()
    TIPOS_DESCUENTO = (
        ('0', 'ESTÁNDAR'),
        ('1', 'ESTUDIANTE'),
        ('2', 'PUEBLO ORIGINARIO')
    )

    codigo = models.CharField(max_length=3, null=False, blank=False, default='000', verbose_name='Código perfil')
    pais = models.CharField(max_length=2, null=True, blank=True, choices=PAISES, verbose_name='País')
    comuna = models.CharField(max_length=5, null=True, blank=True, choices=COMUNAS, verbose_name='Comuna')
    nombre_organizacion = models.CharField(max_length=255, null=True, blank=True, default='Ninguno', verbose_name='Nombre organización')
    tipo_organizacion = models.CharField(max_length=255, null=True, blank=True, default='Cuenta individual', choices=TIPOS_ORGANIZACION, verbose_name='Tipo organización')
    tipo_descuento = models.CharField(max_length=50, null=True, blank=True, default='0', choices=TIPOS_DESCUENTO, verbose_name='Tipo descuento')
    descuento_creactiva = models.BooleanField(default=False, verbose_name='Descuento Creactiva')
    user = models.OneToOneField(
        User,
        related_name='perfil_usuario',
        on_delete=models.CASCADE,
        verbose_name='Usuario'
    )
    estado_capitulo = models.ManyToManyField(
        Capitulo,
        through='cursos.EstadoCapitulo',
        related_name='est_cap'
    )
    visualizacion_capitulo = models.ManyToManyField(
        Capitulo,
        through='cursos.Visualizacion',
        related_name='vis_cap'
    )

    def __str__(self):
        nombre = self.user.first_name
        apellido = self.user.last_name
        usuario = self.user.email
        tipo = self.codigo
        return f'{nombre} {apellido} | Username: {usuario} | Código: {tipo} | Descuento Creactiva: {self.descuento_creactiva}'

class Contacto(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nombre')
    apellido = models.CharField(max_length=255, null=True, blank=True, verbose_name='Apellido')
    email = models.EmailField(max_length=255, null=True, blank=True, verbose_name='Correo')
    mensaje = models.TextField(null=True, blank=True, verbose_name='Mensaje')

    def __str__(self):
        nombre = self.nombre
        apellido = self.apellido
        usuario = self.email
        return f'{nombre} {apellido} | Correo: {usuario}'
