from django.shortcuts import render, HttpResponse
from Productos.models import Producto

# Create your views here.

def home(request):
    return render(request, "ProyectowebApp/home.html")

def productos(request):
    pro= Producto.objects.all()
    return render(request, "ProyectowebApp/productos.html",{"pro":pro})

def tienda(request):
    return render(request, "ProyectowebApp/tienda.html")

def acerca(request):
    return render(request, "ProyectowebApp/acerca.html")

def contacto(request):
    return render(request, "ProyectowebApp/contacto.html")