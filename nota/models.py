from django.db import models
from usuario.models import *

class Examen(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.CharField(max_length=250, verbose_name="Descripción")
    fecha = models.DateField(verbose_name="Fecha")

    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Examenes"
    def __str__(self):
        return self.nombre
    

class Nota(models.Model):
    examen = models.ForeignKey(Examen, verbose_name="Nombre", on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante, verbose_name="Lista de estudiantes", through="NotaDetalle")

    class Meta:
        verbose_name = "Nota Estudiante"
        verbose_name_plural = "Notas de Estudiantes"

    def __str__(self):
        return f"{self.examen.nombre} - {self.examen.fecha}"


class NotaDetalle(models.Model):
    nota = models.ForeignKey(Nota, verbose_name="Examen", on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante,verbose_name="Estudiante", on_delete=models.CASCADE)
    puntaje = models.IntegerField(verbose_name="Puntaje")