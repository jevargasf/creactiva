from django.db import models
from django.contrib.auth.models import User
from cursos.models import Capitulo

class Perfil(models.Model):
    codigo = models.CharField(max_length=3, null=False, blank=False, default='100', verbose_name='Código perfil')
    comuna = models.CharField(max_length=255, null=True, blank=True, verbose_name='Comuna')
    region = models.CharField(max_length=255, null=True, blank=True, verbose_name='Región')
    telefono = models.CharField(max_length=12, null=True, blank=True, verbose_name='Teléfono')
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
        return f'{nombre} {apellido} | Username: {usuario} | Código: {tipo}'

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
