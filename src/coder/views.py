from ast import Return
import re
from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Curso, Estudiante,Profesor,Entregable


def inicio(request):
    
    context = {
        "mensaje":"La comision 40150 es la mejor!",
        "mensaje_bienvenida": "Bienvenidos"
    }
    

    return render(request,"coder/index.html", context)

def estudiante(request):
    return HttpResponse('Vista del estudiante')


def profesor(request):
    return HttpResponse('Vista del profesor')

def entregable(request):
    return HttpResponse('Vista del entregable')

def cursos(request):
    cursos = Curso.objects.all()
    
    context = {
        "mensaje":"Bienvenidos",
        "mensaje_bienvenida": "Nuestros cursos al mejor precio"
    }

    return render(request,"coder/cursos.html",context)

def crear_curso(request):
    
    if request.method == "GET":
        return render(request,"coder/formulario.html")
    else:
        nombre = request.POST["nombre"]
        camada = request.POST["camada"]
        curso = Curso(nombre=nombre,camada = camada)
        
        curso.save()
        return render(request,"coder/index.html")


def fake_login(request):
    if request.method== 'GET':
        
     
       return render(request,"coder/login.html")

    else: 
        username = request.POST["username"]
        password = request.POST["password"]
        
        if username == "admin" and password == "12345":
            return HttpResponse("Bienvenido Admin")
        else:
            return HttpResponse("No te conozco")
        
 
