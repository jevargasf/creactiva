from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    codigo_perfil = models.CharField(max_length=3, null=False, blank=False)
    comuna = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=12, null=True, blank=True)
    user = models.OneToOneField(
        User,
        related_name='perfil',
        on_delete=models.CASCADE
    )

    def __str__(self):
        nombre = self.user.first_name
        apellido = self.user.last_name
        usuario = self.user.email
        tipo = self.codigo_perfil
        return f'{nombre} {apellido} | {usuario} | {tipo}'