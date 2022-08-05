from ast import Return
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