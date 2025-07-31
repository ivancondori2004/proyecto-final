from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import Producto

# Agregar producto al carro
def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Tienda")  

# Eliminar producto del carro
def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Tienda")

# Restar cantidad de un producto en el carro
def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Tienda")

# Limpiar todo el carro 
def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda")