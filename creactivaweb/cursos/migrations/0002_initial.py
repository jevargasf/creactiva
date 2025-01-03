# Generated by Django 5.1 on 2024-12-07 23:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cursos', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadocapitulo',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_est', to='main.perfil', verbose_name='perfiles'),
        ),
        migrations.AddField(
            model_name='curso',
            name='eti',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etiquetas', to='cursos.etiqueta', verbose_name='Etiqueta'),
        ),
        migrations.AddField(
            model_name='curso',
            name='idi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='idiomas', to='cursos.idioma', verbose_name='Idioma'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='mat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materiales', to='cursos.materialescomplementario', verbose_name='Materiales complementarios'),
        ),
        migrations.AddField(
            model_name='visualizacion',
            name='capitulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capitulo_vis', to='cursos.capitulo', verbose_name='capitulo'),
        ),
        migrations.AddField(
            model_name='visualizacion',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_vis', to='main.perfil', verbose_name='perfil'),
        ),
    ]
