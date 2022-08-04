from ast import Return
from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Curso, Estudiante,Profesor,Entregable


def inicio(request):
    return render(request,"coder/index.html", {"mensaje":"La comision 40150 es la mejor!"})

def estudiante(request):
    return HttpResponse('Vista del estudiante')


def profesor(request):
    return HttpResponse('Vista del profesor')

def entregable(request):
    return HttpResponse('Vista del entregable')

def cursos(request):

    cursos = Curso.objects.all()
    
    lista_cursos_nombres = []

    for curso in cursos:
        lista_cursos_nombres.append(curso.nombre)

    return HttpResponse(lista_cursos_nombres)