from django.contrib import admin
from django.utils.html import format_html
from nota.models import *


class EstudianteInline(admin.TabularInline):
    model = NotaDetalle
    extra = 0
    autocomplete_field = ('estudiante',)
    can_delete = False


class NotaAdmin(admin.ModelAdmin):
    inlines = [EstudianteInline]
    list_display = ('examen', 'get_estudiantes', 'get_puntajes',)
    search_fields = ('fecha', 'examen',)
    list_filter = ('examen',)
    
    def get_estudiantes(self, obj):
        estudiantes = obj.estudiantes.all()
        nombres = [e.nombre + " " + e.apellido for e in estudiantes]
        return format_html("</br> ".join(nombres))
    
    def get_puntajes(self, obj):
        nota_detalles = obj.notadetalle_set.all()
        puntajes = [str(detalle.puntaje) for detalle in nota_detalles]
        return format_html("</br> ".join(puntajes))

    get_estudiantes.short_description = 'Estudiantes'
    get_puntajes.short_description = 'Puntajes'

admin.site.register(Nota, NotaAdmin) 


class ExamenAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
admin.site.register(Examen, ExamenAdmin)

