from django.db import models

class Etiqueta(models.Model):
    id_eti = models.AutoField(primary_key=True, null=False)
    nom_eti = models.CharField(max_length=50)

class MaterialComplementario(models.Model):
    id_mat = models.AutoField(primary_key=True, null=False)
    nom_mat = models.CharField(max_length=255)
    lin_mat = models.URLField()

class Capitulo(models.Model):
    id_cap = models.AutoField(primary_key=True, null=False)
    nom_cap = models.CharField(max_length=255)
    des_cap = models.TextField()
    lin_cap = models.URLField()
    id_lin = models.ForeignKey(
        MaterialComplementario,
        blank=True, 
        null=True,
        on_delete=models.CASCADE,
        related_name='materiales'
    )

class Curso(models.Model):
    id_cur = models.AutoField(primary_key=True, null=False)
    nom_cur = models.CharField(max_length=255)
    des_cur = models.TextField()
    id_eti = models.ForeignKey(
        Etiqueta,
        on_delete=models.CASCADE,
        related_name='etiquetas'
    )
    id_cap = models.ForeignKey(
        Capitulo,
        on_delete=models.CASCADE,
        related_name='capitulos'
    )

