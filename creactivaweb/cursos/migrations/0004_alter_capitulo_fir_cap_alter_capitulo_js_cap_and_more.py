# Generated by Django 5.1 on 2024-12-22 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_capitulo_fir_cap_capitulo_js_cap_capitulo_thu_cap_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitulo',
            name='fir_cap',
            field=models.CharField(max_length=255, null=True, verbose_name='Link frame preview'),
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='js_cap',
            field=models.CharField(max_length=255, null=True, verbose_name='Link xml.js'),
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='lin_cap',
            field=models.URLField(max_length=255, verbose_name='Link capítulo'),
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='thu_cap',
            field=models.CharField(max_length=255, null=True, verbose_name='Link thumbnail'),
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='xml_cap',
            field=models.CharField(max_length=255, null=True, verbose_name='Link xml'),
        ),
    ]
