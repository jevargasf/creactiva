# Generated by Django 5.1 on 2024-12-22 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitulo',
            name='fir_cap',
            field=models.URLField(null=True, verbose_name='Link frame preview'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='js_cap',
            field=models.URLField(null=True, verbose_name='Link xml.js'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='thu_cap',
            field=models.URLField(null=True, verbose_name='Link thumbnail'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='xml_cap',
            field=models.URLField(null=True, verbose_name='Link xml'),
        ),
    ]
