from django.contrib import admin
from asistencia.models import *
from django.utils.html import format_html


class EstudianteInline(admin.TabularInline):
    model = AsistenciaEstudianteDetalle
    extra = 0
    autocomplete_field = ('asis_estudiante',)
    can_delete = False



class AsistenciaEstudianteAdmin(admin.ModelAdmin):
    inlines = [EstudianteInline]
    list_display = ('fecha', 'horario', 'estudiantes', 'presentes',) 
    search_fields = ('fecha',)
    exclude = ('fecha',)
    list_filter = ('fecha', 'horario',)
    def estudiantes(self, obj):
        return format_html("</br>".join([ae.nombre+" "+ae.apellido for ae in obj.asistencia_estudiante.all()]))
    def presentes(self, obj):
        estudiantes = obj.asistenciaestudiantedetalle_set.all()
        estados = ["Presente" if est.presente else "Falto" for est in estudiantes]
        estados_str = "</br>".join(estados)
        return format_html(estados_str)
    presentes.short_description = "Presente"
admin.site.register(AsistenciaEstudiante, AsistenciaEstudianteAdmin) 


class AsistenciaDocenteAdmin(admin.ModelAdmin):
    list_display = ('docente', 'fecha', 'horario',)
    # list_per_page = 10
    search_fields = ('docente', 'fecha',)
    exclude = ('fecha',)
    list_filter = ('docente', 'fecha',)
admin.site.register(AsistenciaDocente, AsistenciaDocenteAdmin) 
