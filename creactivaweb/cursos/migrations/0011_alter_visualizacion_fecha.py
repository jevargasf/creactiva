# Generated by Django 5.1 on 2025-01-09 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0010_capitulo_desc_corta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualizacion',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Última visualización'),
        ),
    ]
