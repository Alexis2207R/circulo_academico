from django.contrib import admin
from horario.models import *


class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo_curso', 'nombre', 'descripcion',) 
    search_fields = ('nombre',)
admin.site.register(Curso, CursoAdmin) 


class HorarioAdmin(admin.ModelAdmin):
    list_display = ('curso', 'duracion', 'dia_semana', 'hora_inicio', 'hora_fin',) 
    search_fields = ('curso', 'duracion',)
    exclude = ('hora_fin',)
    list_filter = ('curso', 'duracion', 'dia_semana', 'hora_inicio', 'hora_fin',) 
admin.site.register(Horario, HorarioAdmin) 