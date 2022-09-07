from django.shortcuts import render
from .forms import *
from .models import *



from django.http import HttpResponse
def form(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'registro.html',{'form':form})

    else:
        form = UsuarioForm()
        return render(request,'registro.html',{'form':form})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def contactenos(request):
    if request.method=='POST':
        contactenos = ContactoForm(request.POST)
        if contactenos.is_valid():
            contactenos.save()
            return render(request, 'contactenos.html', {'contactenos': contactenos})
    else:
        contactenos=ContactoForm()

        return render(request, 'contactenos.html', {'contactenos': contactenos})