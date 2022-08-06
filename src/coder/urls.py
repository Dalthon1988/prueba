from django.urls import path 
from coder.views import *

urlpatterns = [
     path("",inicio , name="inicio"),
     path("cursos/", cursos, name= "cursos"),
     path("estudiantes/", estudiante, name="estudiante"),
     path("profesores/", profesor,  name= "profesores"),
     path("entregables/",entregable, name= "entregable"),
     path("curso/crear/",crear_curso, name= "curso_crear"),
     path("login/", fake_login, name= "Login_Falso" )  
]