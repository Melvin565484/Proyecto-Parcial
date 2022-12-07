from django.shortcuts import render, redirect
from django.template import context
from django.http import HttpResponse
from .models import tblClientes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')

def index(request):
    return render(request,'index.html')

def about2(request):
    return render(request,'about2.html')

def pedidos(request):
    return render(request,'pedidos.html')

def vistalogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('home')

    return render(request,'login.html')

def cerrarsesion(request):
    logout(request)
    return redirect('/')

def formulario1(request):
    return render(request,'formulario1.html',{"Pastel1":"Personalizado"})

def clientes(request):
    clientes = tblClientes.objects.all()
    return render(request,'clientescrud.html',{"clientes":clientes})

class Registro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2', 'email', 'first_name', 'last_name']

def registro(request):
    form = Registro()
    if request.method == 'POST':
        form = Registro(request.POST)
        if  form.is_valid():
            form.save()
    return render(request,'register.html', {"form":form})

def addclientes(request):
    codigo=request.POST['inputcodigo']
    nombre=request.POST['inputnombre']
    apellido=request.POST['inputapellido']
    direccion=request.POST['inputdireccion']

    clientes= tblClientes.objects.create(
            id_cliente=codigo, nombre=nombre, apellido=apellido, factura=direccion
    )
    return redirect('/clientes')


def editcliente(request,id):
    clientes=tblClientes.objects.get(id=id)

    return render(request,'editcliente.html',{"clientes":clientes})

def guardarcliente(request,id):
    codigo=request.POST['inputcodigo']
    nombre=request.POST['inputnombre']
    apellido=request.POST['inputapellido']
    direccion=request.POST['inputdireccion']

    id=tblClientes.objects.get(id=id)
    id.id_cliente=codigo
    id.nombre=nombre
    id.apellido=apellido
    id.factura=direccion
    id.save()
    return redirect('/clientes')

def delcliente(request,id):
    clientes=tblClientes.objects.get(id=id)
    clientes.delete()
    return redirect('/clientes')