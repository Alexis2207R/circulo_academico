# Generated by Django 4.2.2 on 2023-06-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistenciaestudiante',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha y Hora'),
        ),
    ]
