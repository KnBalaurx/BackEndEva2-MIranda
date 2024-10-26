from django.shortcuts import render
from django.shortcuts import redirect
from clienteApp.models import Cliente
from clienteApp.forms import FormCliente


def index(request):
    return render(request, 'index.html')

def Tabla(request):
    cliente = Cliente.objects.all()
    data = {'cliente': cliente}
    return render(request, 'tabla.html', data)

def agClientes(request):
    form = FormCliente()
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
    data = {'form': form}
    return render(request, 'agCliente.html', data)

def actualizarCli(request, id):
    cliente =  Cliente.objects.get(id = id)
    form = FormCliente(instance= cliente)
    if request.method == 'POST':
        form = FormCliente(request.POST, instance= cliente)
        if form.is_valid():
            form.save()
        return Tabla(request)
    data = {'form': form}
    return render(request, 'agCliente.html', data)

def borrarCli(request, id):
    cliente =  Cliente.objects.get(id = id)
    cliente.delete()
    return redirect('/princi')
