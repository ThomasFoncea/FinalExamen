from django.shortcuts import render, redirect
from .models import noticias
from .forms import NoticiaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
# Create your views here.


def paginaprincipal(request):
    return render(request,'paginaprincipal.html')

def contacto(request):
    return render(request,'contacto.html')

def deporte(request):
    return render(request,'deporte.html')

def login(request):
    return render(request,'login.html')

def nacional(request):
    return render(request,'nacional.html')

def policial(request):
    return render(request,'policial.html')

def recuperarcontraseña(request):
    return render(request,'recuperarcontraseña.html')

def tendencia(request):
    return render(request,'tendencia.html')

def nueva_noticia(request):

    formulario = NoticiaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('/')

    return render(request,'crud/nuevanoticia.html',{"formulario":formulario})

def gesNoticia(request):
    Noticias = noticias.objects.all()
    context={"noticias":Noticias}
    return render(request,'crud/gestion.html',context)

def editarnoti(request, codigo):
    Noticias = noticias.objects.get(codigo=codigo)
    formulario = NoticiaForm(request.POST or None, request.FILES or None, instance=Noticias)
    if formulario.is_valid() and request.POST:
       formulario.save()
       return redirect('gestion')
    return render(request, "crud/modificar.html", {"formulario": formulario})


def borrarnoticias(request, codigo):
    Noticias = noticias.objects.get(codigo=codigo)
    Noticias.delete()
    messages.success(request, '¡Noticia Eliminada!')
    return redirect('gestion')