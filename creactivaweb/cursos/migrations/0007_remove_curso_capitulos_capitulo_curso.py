# Generated by Django 5.1 on 2024-12-26 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_curso_imagen_portada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='capitulos',
        ),
        migrations.AddField(
            model_name='capitulo',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curso', to='cursos.curso', verbose_name='Curso'),
        ),
    ]
