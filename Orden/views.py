from .orden import Orden
from modelos.models import Producto
from django.shortcuts import redirect, render
from .models import Compra, CompraItem

def agregar_producto(request,producto_id):
    orden = Orden(request)
    producto=Producto.objects.get(id=producto_id)
    orden.agregar(producto)
    return redirect('productos')

def eliminar_producto(request,producto_id):
    orden=Orden(request)
    producto=Producto.objects.get(id=producto_id)
    orden.eliminar(producto)
    return redirect('productos')

def restar_producto(request,producto_id):
    orden=Orden(request)
    producto=Producto.objects.get(id=producto_id)
    orden.restar(producto)
    return redirect('productos')

def limpiar_orden(request):
    orden=Orden(request)
    orden.limpiar_orden()
    return redirect('productos')

def procesar_pedido(request):
    orden = Orden(request)

    if request.method == 'POST':
        nuevacompra = Compra()
        nuevacompra.usuario = request.user
        nuevacompra.direccion = request.POST.get('direccion')
        nuevacompra.lugar = request.POST.get('lugar')
        nuevacompra.telefono = request.POST.get('telefono')
        nuevacompra.total = request.POST.get('total')
        nuevacompra.save()
        for item in orden:
            a = CompraItem(
                compra=nuevacompra,
                producto=item['nombre'],
                precio=item['precio'],
                cantidad=item['cantidad'],
            )
            a.save()
        orden.limpiar_orden()
        return render(request, 'ordencreada.html', {'compra': nuevacompra})
    else:

        return render(request, 'crearorden.html', {'orden': Orden})