from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages


def home(request):
    cursos_listados = Curso.objects.all()
    
    messages.success(request, "¡Cursos Listados!")
    
    return render(request, "gestion_cursos.html", {"cursos": cursos_listados})


def registrar_curso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCreditos']

    curso = Curso.objects.create(
        codigo = codigo,
        nombre = nombre,
        creditos = creditos,
    )
    
    messages.success(request, "¡Curso Registrado!")
    
    return redirect('/')


def edicion_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    
    return render(request, "edicion_cursos.html", {"curso": curso})


def editar_curso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, "¡Curso Actualizado!")

    return redirect('/')


def eliminar_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    
    messages.success(request, "¡Curso Eliminado!")
    
    return redirect('/')
