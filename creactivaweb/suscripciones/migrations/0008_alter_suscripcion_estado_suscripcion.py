# Generated by Django 5.1 on 2025-01-26 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suscripciones', '0007_alter_suscripcion_fecha_termino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscripcion',
            name='estado_suscripcion',
            field=models.CharField(default=0, max_length=1, verbose_name='Estado suscripción'),
        ),
    ]
