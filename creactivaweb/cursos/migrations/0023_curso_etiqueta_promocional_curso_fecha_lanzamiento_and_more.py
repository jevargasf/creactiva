# Generated by Django 5.1 on 2025-02-19 19:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0022_alter_capitulo_etiqueta_promocional'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='etiqueta_promocional',
            field=models.CharField(blank=True, choices=[('0', '--- NINGUNO ---'), ('1', 'ESTRENO'), ('2', 'PRÓXIMAMENTE')], default='0', max_length=1, null=True, verbose_name='Etiqueta promocional'),
        ),
        migrations.AddField(
            model_name='curso',
            name='fecha_lanzamiento',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Fecha lanzamiento'),
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='etiqueta_promocional',
            field=models.CharField(blank=True, choices=[('0', '--- NINGUNO ---'), ('1', 'ESTRENO'), ('2', 'PRÓXIMAMENTE')], default='0', max_length=1, null=True, verbose_name='Etiqueta promocional'),
        ),
    ]
