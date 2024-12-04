from django.db import models

class Etiqueta(models.Model):
    id_eti = models.AutoField(primary_key=True, null=False, verbose_name='ID Etiqueta')
    nom_eti = models.CharField(max_length=50, verbose_name='Nombre etiqueta')

    def __str__(self):
        return f'{self.nom_eti}'

class MaterialComplementario(models.Model):
    id_mat = models.AutoField(primary_key=True, null=False, verbose_name='ID material')
    nom_mat = models.CharField(max_length=255, verbose_name='Nombre material')
    lin_mat = models.URLField(verbose_name='Link material')

    def __str__(self):
        return f'{self.nom_mat}'

class Capitulo(models.Model):
    id_cap = models.AutoField(primary_key=True, null=False, verbose_name='ID capítulo')
    num_cap = models.IntegerField(null=True, blank=True, verbose_name='Número capítulo')
    nom_cap = models.CharField(max_length=255, verbose_name='Nombre capítulo')
    des_cap = models.TextField(verbose_name='Descripción')
    lin_cap = models.URLField(verbose_name='Link capítulo')
    id_lin = models.ForeignKey(
        MaterialComplementario,
        blank=True, 
        null=True,
        on_delete=models.CASCADE,
        related_name='materiales',
        verbose_name='Material asociado'
    )

    def __str__(self):
        return f'Número: {self.num_cap} | {self.nom_cap}'

class Curso(models.Model):
    id_cur = models.AutoField(primary_key=True, null=False, verbose_name='ID curso')
    nom_cur = models.CharField(max_length=255, verbose_name='Nombre curso')
    des_cur = models.TextField(verbose_name='Descripción')
    id_eti = models.ForeignKey(
        Etiqueta,
        on_delete=models.CASCADE,
        related_name='etiquetas',
        verbose_name='Etiqueta'
    )
    id_cap = models.ForeignKey(
        Capitulo,
        on_delete=models.CASCADE,
        related_name='capitulos',
        verbose_name='Capítulo'
    )

    def __str__(self):
        return f'{self.nom_cur}'