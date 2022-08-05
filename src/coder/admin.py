from tkinter import E
from django.contrib import admin
from coder.models import Curso
from coder.views import Curso,Entregable,Profesor,Estudiante


# Register your models here.
admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Estudiante)
admin.site.register(Profesor)
