from django.contrib import admin
from django.urls import path
from app_Compras.views import *
from app_Inicio.views import  inicio2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio2, name="home"),
    path('acerca/',about2, name="about"),
    path('pedidos/',pedidos, name="pedidos"),
    path('login/',vistalogin, name="login"),
    path('logout/',cerrarsesion, name="logout"),
    path('Formulario/',formulario1, name="formulario1"),
    path('clientes/',clientes, name="clientescrud"),
    path('addclientes/',addclientes, name="addclientes"),
    path('delcliente/<id>',delcliente, name="delcliente"),
    path('editcliente/<id>',editcliente, name="editcliente"),
    path('guardarcliente/<id>',guardarcliente, name="guardarcliente"),
    path('registro/',registro, name="registro")
]
