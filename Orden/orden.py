from modelos.models import Producto
from decimal import Decimal
class Orden:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        orden=self.session.get('orden')
        if not orden:
            self.session['orden']={}
            self.orden = self.session['orden']
        else:
            self.orden= orden

    def agregar(self, producto):
        id= str(producto.id)
        if id not in self.orden.keys():
            self.orden[id]={
                'producto_id':producto.id,
                'nombre':producto.nombre,
                'precio':producto.precio,
                'cantidad':1,
            }
        else:
            self.orden[id]["cantidad"]+= 1
            self.orden[id]["precio"]+= producto.precio
        self.guardar_orden()

    def guardar_orden(self):
        self.session['orden'] = self.orden
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.orden:
            del self.orden[id]
            self.guardar_orden()

    def restar(self, producto):
        id=str(producto.id)
        if id in self.orden.keys():
            self.orden[id]["cantidad"] -= 1
            self.orden[id]["precio"] -= producto.precio
            if self.orden[id]["cantidad"] < 1:
                self.eliminar(producto)
            self.guardar_orden()

    def limpiar_orden(self):
        self.session['orden'] = {}
        self.session.modified = True

    def __iter__(self):

        producto_ids = self.orden.keys()
        productos = Producto.objects.filter(id__in=producto_ids)
        orden = self.orden.copy()
        for producto in productos:
            orden[str(producto.id)]['nombre'] = producto
        for item in orden.values():
            item['precio'] = item['precio']
            yield item

    def get_total_orden(self):

        return sum(Decimal(item['precio']) for item in self.orden.values())
