from django.shortcuts import render
from front.models import ProductosInicio, ProductosJugueteria

# Create your views here.


def index (request):
    return render(request, 'index.html')

def accesorios (request):
    return render(request, 'accesorios.html')

def jugueteria (request):
    return render(request, 'jugueteria.html')

def miraGatos (request):
    return render(request, 'gatosapi.html')

def login (request):
    return render(request, 'back/templates/login.html')

def registro (request):
    return render(request, 'registro.html')

def pppliveclear (request):
    return render(request, 'pro_plan_gato_liveclear.html')

def index(request):
    fotos = ProductosInicio.objects.all()
    datos = {'productos' : fotos}
    return render(request, 'index.html', datos)

def jugueteria(request):
    fotos = ProductosJugueteria.objects.all()
    datos = {'productos' : fotos}
    return render(request, 'jugueteria.html', datos)