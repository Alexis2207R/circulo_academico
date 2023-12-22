from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime, timedelta
from usuario.models import *


class Curso(models.Model):
    codigo_curso = models.CharField(max_length=10, unique=True, null=True, blank=True, verbose_name="Código")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    dia_semana_choices = (
        ('L', 'Lunes'),
        ('M', 'Martes'),
        ('MI', 'Miércoles'),
        ('J', 'Jueves'),
        ('V', 'Viernes'),
        ('S', 'Sábado'),
        ('D', 'Domingo'),
    )

    curso = models.ForeignKey(Curso, verbose_name="Curso", on_delete=models.CASCADE, null=True)
    docente = models.ForeignKey(Docente, verbose_name="Docente", on_delete=models.CASCADE, null=True)
    dia_semana = models.CharField(max_length=2, choices=dia_semana_choices, null=True)
    hora_inicio = models.TimeField(null=True, verbose_name="Hora de Inicio")
    duracion = models.IntegerField(null=True, verbose_name="Duración (minutos)")
    hora_fin = models.TimeField(null=True, blank=True, verbose_name="Hora de fin")

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horario"

    def __str__(self):
        return f"{self.curso.nombre} | Docente: {self.docente.nombre} {self.docente.apellido} | {self.get_dia_semana_display()}: {self.hora_inicio} - {self.hora_fin}"

@receiver(pre_save, sender=Horario)
def calcular_hora_fin(sender, instance, **kwargs):
    if instance.hora_inicio and instance.duracion:
        inicio = datetime.combine(datetime.today(), instance.hora_inicio)
        fin = inicio + timedelta(minutes=instance.duracion)
        instance.hora_fin = fin.time()