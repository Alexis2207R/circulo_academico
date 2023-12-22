from django.contrib import admin
from usuario.models import *
from asistencia.models import *

from django.contrib.auth.views import PasswordChangeView, LogoutView
from django.urls import reverse_lazy

# from jazzmin.utils import get_jazzmin_model


class MyPasswordChangeView(PasswordChangeView):
    template_name = "admin/my_password_change.html"
    success_url = reverse_lazy("admin:index")


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("admin:index")


admin.site.login_view = "admin:index"
admin.site.logout_view = "admin:logout"


class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        "codigo_estudiante",
        "user",
        "nombre",
        "apellido",
        "carrera_interes",
        "fecha_nacimiento",
        "mostrar_asistencia",
    )
    search_fields = ("user", "nombre", "apellido", "codigo_estudiante")

    def mostrar_asistencia(self, obj):
        asistencias = AsistenciaEstudianteDetalle.objects.filter(estudiante=obj)
        return ", ".join([str(asistencia.presente) for asistencia in asistencias])

    mostrar_asistencia.short_description = "Asistencia"


admin.site.register(Estudiante, EstudianteAdmin)


class DocenteAdmin(admin.ModelAdmin):
    list_display = (
        "codigo_docente",
        "user",
        "nombre",
        "apellido",
    )
    search_fields = ("user", "nombre", "apellido", "codigo_docente")


admin.site.register(Docente, DocenteAdmin)
