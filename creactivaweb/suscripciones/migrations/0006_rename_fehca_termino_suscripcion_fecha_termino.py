# Generated by Django 5.1 on 2025-01-23 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suscripciones', '0005_remove_solicitudorganizacion_apellido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suscripcion',
            old_name='fehca_termino',
            new_name='fecha_termino',
        ),
    ]
