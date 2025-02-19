# Generated by Django 5.1 on 2025-02-19 13:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0020_capitulo_etiqueta_promocional_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitulo',
            name='fecha_lanzamiento',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Fecha lanzamiento'),
        ),
    ]
