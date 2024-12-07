from django.db import models
from django.contrib.auth.models import User
from cursos.models import Capitulo

class Perfil(models.Model):
    cod_per = models.CharField(max_length=3, null=False, blank=False, default='100', verbose_name='Código perfil')
    com_per = models.CharField(max_length=255, null=True, blank=True, verbose_name='Comuna')
    reg_per = models.CharField(max_length=255, null=True, blank=True, verbose_name='Región')
    tel_per = models.CharField(max_length=12, null=True, blank=True, verbose_name='Teléfono')
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
        tipo = self.cod_per
        return f'{nombre} {apellido} | Username: {usuario} | Código: {tipo}'