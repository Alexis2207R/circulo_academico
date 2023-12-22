from django.db import models
from django.contrib.auth.models import User
from horario.models import *
from usuario.models import *


class AsistenciaEstudiante(models.Model):
    asistencia_estudiante = models.ManyToManyField(Estudiante, verbose_name="Estudiante", through="AsistenciaEstudianteDetalle")
    horario = models.ForeignKey(Horario, verbose_name="Horario", on_delete=models.CASCADE, null=True)
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha", null=True, blank=True) 

    class Meta:
        verbose_name = "Asistencia Estudiante"
        verbose_name_plural = "Asistencia de Estudiantes"

    def __str__(self):
        return f"{self.horario.curso.nombre} - {self.fecha}"


class AsistenciaEstudianteDetalle(models.Model):
    asis_estudiante = models.ForeignKey(AsistenciaEstudiante, verbose_name="Asistencias", on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, verbose_name="Estudiante", on_delete=models.CASCADE)
    presente = models.BooleanField(default=True, verbose_name="Presente")


class AsistenciaDocente(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, verbose_name="Docente")
    horario = models.ForeignKey(Horario, verbose_name="Horario", on_delete=models.CASCADE, null=True)
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha", null=True, blank=True)
    presente = models.BooleanField(default=True, verbose_name="Presente")

    class Meta:
        verbose_name = "Asistencia Docente"
        verbose_name_plural = "Asistencias de Docentes"

    def __str__(self):
        return f"{self.docente.user.username} - {self.horario.curso.nombre} - {self.fecha}"
