from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    
    SEXO = (
        ("M", "Masculino"),
        ("F", "Femenino"),
    )
    N_EDUCATIVO = (
        ("P", "Primaria"),
        ("S", "Secundaria"),
        ("SC", "Secundaria culminada"),
    )

    codigo_estudiante = models.CharField(max_length=8, unique=True, null=True, verbose_name="DNI")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name="Usuario")
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    apellido = models.CharField(verbose_name="Apellido", max_length=100)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento", auto_now=False, auto_now_add=False)
    sexo = models.CharField(verbose_name="Sexo", max_length=1, choices=SEXO)
    direccion_residencia = models.CharField(verbose_name="Dirección", max_length=50)
    telefono = models.CharField(verbose_name="Número celular", max_length=20)
    correo = models.CharField(verbose_name="Correo", max_length=50)
    nivel_educativo = models.CharField(verbose_name="Nivel Educativo", max_length=50, choices=N_EDUCATIVO)
    escuela_procedencia = models.CharField(verbose_name="Escuela de Procedencia", max_length=200)
    telefono_emergencia = models.CharField(verbose_name="Telefono de Emergencia", max_length=20)
    carrera_interes = models.CharField(verbose_name="Carrera de Interes", max_length=100)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return f"Código: {self.codigo_estudiante} | Nombre: {self.nombre} {self.apellido}"


class Docente(models.Model):
    SEXO = (
        ("M", "Masculino"),
        ("F", "Femenino"),
    )

    codigo_docente = models.CharField(max_length=8, unique=True, null=True, verbose_name="DNI")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name="usuario")
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    apellido = models.CharField(verbose_name="Apellido", max_length=10)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento", auto_now=False, auto_now_add=False)
    sexo = models.CharField(verbose_name="Sexo", max_length=1, choices=SEXO)
    direccion_residencia = models.CharField(verbose_name="Dirección", max_length=50)
    telefono = models.CharField(verbose_name="Numero celular", max_length=20)
    correo = models.CharField(verbose_name="Correo", max_length=50)

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return f"Código: {self.codigo_docente} | Nombre: {self.nombre} {self.apellido}"