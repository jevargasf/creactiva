# Generated by Django 5.1 on 2025-02-17 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suscripciones', '0025_remove_suscripcion_codigo_validacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilcodigo',
            name='estado_uso_codigo',
            field=models.CharField(default='0', max_length=1, verbose_name='Estado uso código'),
        ),
    ]
