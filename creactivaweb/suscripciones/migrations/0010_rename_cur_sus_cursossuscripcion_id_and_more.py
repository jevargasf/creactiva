# Generated by Django 5.1 on 2025-01-27 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suscripciones', '0009_rename_sus_suscripcion_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursossuscripcion',
            old_name='cur_sus',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='perfilsuscripcion',
            old_name='usu_sus',
            new_name='id',
        ),
    ]
