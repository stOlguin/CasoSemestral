"""Prueba1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from front.views import index
from front.views import accesorios
from front.views import jugueteria
from front.views import miraGatos
#from front.views import iniciarSesion <<<Descomentar luego>>>
from front.views import registro
from front.views import pppliveclear
from back.views import indexBack, login, validarUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index.html', index),
    path('accesorios.html', accesorios),
    path('jugueteria.html', jugueteria),
    path('gatosapi.html', miraGatos),
    #path('iniciar_sesion.html', iniciarSesion),
    path('registro.html', registro),
    path('pro_plan_gato_liveclear.html', pppliveclear),
    path('login.html', login),
    path('validarUsuario/', validarUsuario),
    path('index_back.html', indexBack)
]
