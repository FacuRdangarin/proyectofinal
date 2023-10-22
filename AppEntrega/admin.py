from django.contrib import admin
from .models import Curso,Estudiante,Profesor,Avatar,Entregable,Blog

# Register your models here.
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Avatar)
admin.site.register(Blog)
admin.site.register(Entregable)

