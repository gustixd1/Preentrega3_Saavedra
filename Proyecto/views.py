from django.shortcuts import render
from Proyecto.forms import *
from Proyecto.models import *
from django.http import HttpResponse


# Create your views here.

def gatos(request):
    
    if request.method == "POST":
        form = FormGato(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            
            gato = Gato(nombre = info["nombre"], raza = info["raza"], fecha_nacimiento = info["fecha_nacimiento"])
            gato.save()
            return render(request, "Home/index.html", {"mensaje" : f"Su gato ha sido registrado correctamente."})
    else:
        form = FormGato()
    return render(request, "Proyecto/gatos.html", {"form" : form})
        
def perros(request):
    
    if request.method == "POST":
        form = FormPerro(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            
            perro = Perro(nombre = info["nombre"], raza = info["raza"], fecha_nacimiento = info["fecha_nacimiento"])
            perro.save()
            return render(request, "Home/index.html", {"mensaje" : f"Su perro ha sido registrado correctamente."})
    else:
        form = FormPerro()
    return render(request, "Proyecto/perros.html", {"form" : form})

def otraMascota(request):
    
    if request.method == "POST":
        form = FormMascota(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            
            mascota = Mascota(nombre = info["nombre"], especie = info["especie"], fecha_nacimiento = info["fecha_nacimiento"])
            mascota.save()
            return render(request, "Home/index.html", {"mensaje" : f"Su mascota ha sido registrado correctamente."})
    else:
        form = FormMascota()
    return render(request, "Proyecto/mascota.html", {"form" : form})
        

def buscarGato(request):
        return render(request, "Proyecto/buscar_gatos.html")

def buscar(request):

    if request.GET["nombre"]:
        
        nombre = request.GET["nombre"]
        if Gato.objects.filter(nombre__icontains=nombre):
            mascotas = Gato.objects.filter(nombre__icontains=nombre)
            return render(request, "Proyecto/resultado_busqueda.html", {"mascotas" : mascotas, "nombre" : nombre})
        return render(request, "Proyecto/buscar_gatos.html", {"mensaje" : "No se ha encontrado ningún gato con ese nombre."})
        
    else:
        mensaje = "No has ingresado ningún dato."
        return render(request, "Proyecto/buscar_gatos.html", {"mensaje" : mensaje})

