# Generated by Django 5.1 on 2025-02-17 21:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_perfil_descuento_creactiva'),
        ('suscripciones', '0028_alter_perfilsuscripcion_codigo_promocional'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilCodigo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID códigos perfiles')),
                ('estado_uso_codigo', models.CharField(default='0', max_length=1, verbose_name='Estado uso código')),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suscripciones.codigopromocional', verbose_name='ID Código Promocional')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.perfil', verbose_name='ID Perfil')),
            ],
        ),
    ]
