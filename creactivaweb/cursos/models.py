from django.db import models


class Etiqueta(models.Model):
    eti = models.AutoField(primary_key=True, null=False, verbose_name='ID Etiqueta')
    nombre = models.CharField(max_length=50, verbose_name='Nombre etiqueta')

    def __str__(self):
        return self.nombre

class Idioma(models.Model):
    idi = models.AutoField(primary_key=True, null=False, verbose_name='ID idioma')
    nombre = models.CharField(max_length=255, verbose_name='Nombre idioma')

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    aut = models.AutoField(primary_key=True, null=False, verbose_name='ID autor')
    nombre_autor = models.CharField(max_length=255, verbose_name='Nombre autor')

    def __str__(self):
        return self.nombre_autor

class MaterialesComplementario(models.Model):
    mat = models.AutoField(primary_key=True, null=False, verbose_name='ID material')
    nombre_material = models.CharField(max_length=255, verbose_name='Nombre material')
    link_material = models.CharField(max_length=255, null=True, verbose_name='Link material')

    def __str__(self):
        return f'{self.nombre_material}'

class Curso(models.Model):
    cur = models.AutoField(primary_key=True, null=False, verbose_name='ID curso')
    nombre = models.CharField(max_length=255, verbose_name='Nombre curso')
    desc_corta= models.CharField(max_length=255, verbose_name='Descripción Corta')
    desc_larga = models.TextField(verbose_name='Descripción Larga')
    imagen_portada = models.CharField(max_length=255, verbose_name='Imagen portada', null=True)
    etiquetas = models.ForeignKey(
        Etiqueta,
        on_delete=models.CASCADE,
        related_name='etiquetas',
        verbose_name='Etiqueta'
    )
    idiomas = models.ForeignKey(
        Idioma,
        on_delete=models.CASCADE,
        related_name='idiomas',
        verbose_name='Idioma',
        default=1
    )
    autores = models.ManyToManyField(Autor, verbose_name='Autores', related_name='autores')

    def __str__(self):
        return self.nombre

class Capitulo(models.Model):
    cap = models.AutoField(primary_key=True, null=False, verbose_name='ID capítulo')
    numero = models.IntegerField(null=True, verbose_name='Número capítulo')
    nombre = models.CharField(max_length=255, verbose_name='Nombre capítulo')
    duracion = models.IntegerField(verbose_name='Duración (minutos)')
    descripcion = models.TextField(verbose_name='Descripción')
    num_actividades = models.IntegerField(verbose_name='Número de actividades interactivas')
    link = models.URLField(verbose_name='Link capítulo', max_length=255)
    xml_cap = models.CharField(verbose_name='Link xml', null=True, max_length=255)
    js_cap = models.CharField(verbose_name='Link xml.js', null=True, max_length=255)
    thumbnail = models.CharField(verbose_name='Link thumbnail', null=True, max_length=255)
    first_frame = models.CharField(verbose_name='Link frame preview', null=True, max_length=255)
    material = models.ForeignKey(
        MaterialesComplementario,
        blank=True, 
        null=True,
        on_delete=models.CASCADE,
        related_name='materiales',
        verbose_name='Materiales complementarios'
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='curso',
        verbose_name='Curso',
        null=True
    )

    def __str__(self):
        return self.nombre

    
    
class EstadoCapitulo(models.Model):
    est = models.AutoField(primary_key=True, null=False, verbose_name='ID estado capítulo')
    perfil = models.ForeignKey(
        'main.Perfil',
        on_delete=models.CASCADE,
        verbose_name='perfiles',
        related_name='perfil_est'
    )
    capitulo = models.ForeignKey(
        'Capitulo',
        on_delete=models.CASCADE,
        verbose_name='capitulos',
        related_name='capitulo_est'
    )
    estado_capitulo = models.IntegerField(verbose_name='Estado capítulo')

    def __str__(self):
        return f'{self.perfil.user} Estado: {self.estado_capitulo}'

class Visualizacion(models.Model):
    vis = models.AutoField(primary_key=True, null=False, verbose_name='ID visualización')
    perfil = models.ForeignKey(
        'main.Perfil',
        on_delete=models.CASCADE,
        verbose_name='perfil',
        related_name='perfil_vis'
    )
    capitulo = models.ForeignKey(
        'Capitulo',
        on_delete=models.CASCADE,
        verbose_name='capitulo',
        related_name='capitulo_vis'
    )
    fecha = models.DateTimeField(null=False, verbose_name='Última visualización')
    minuto = models.IntegerField(null=False, verbose_name='Minuto última visualización')

    def __str__(self):
        return f'{self.perfil.user} {self.fecha}'