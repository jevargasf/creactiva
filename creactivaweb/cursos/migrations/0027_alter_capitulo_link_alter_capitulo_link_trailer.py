# Generated by Django 5.1 on 2025-03-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0026_alter_capitulo_js_trailer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitulo',
            name='link',
            field=models.CharField(max_length=255, verbose_name='Link capítulo'),
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='link_trailer',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Link trailer'),
        ),
    ]
