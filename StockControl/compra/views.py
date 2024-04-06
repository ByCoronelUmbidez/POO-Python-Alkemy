from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Proveedor
from django.contrib import messages
# Create your views here.

def listar_productos(request):
    productos = Producto.objects.all()
    return render (request, 'productos.html', {'productos': productos})

def listar_proveedores(request):
    proveedor = Proveedor.objects.all()
    messages.success(request, '¡Proveedores listados!')
    return render (request, 'listar_proveedores.html', {'proveedor': proveedor})

    
def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        # Crear el proveedor
        proveedor = Proveedor.objects.create(nombre=nombre, apellido=apellido, dni=dni)

        # Verificar si hay información del producto en la sesión
        if 'producto_info' in request.session:
            producto_info = request.session.pop('producto_info')
            # Crear el proveedor
            proveedor = Proveedor.objects.create(nombre=nombre, apellido=apellido, dni=dni)
            # Crear el producto utilizando la información guardada anteriormente
            Producto.objects.create(nombre=producto_info['nombre'], precio=producto_info['precio'], stock_actual=producto_info['stock_actual'], proveedor=proveedor)
            return redirect('productos')

        # Si no hay información de producto en la sesión, simplemente redirigir a la lista de proveedores
        return redirect('listar_proveedores')

    return render(request, 'nuevo_proveedor.html')

def agregar_producto(request):
    if request.method == 'POST':
        nombre_producto = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock_actual = request.POST.get('stock_actual')
        proveedor_id = request.POST.get('proveedor')  # Obtener el ID del proveedor seleccionado
        proveedor_opcion = request.POST.get('proveedor_seleccionado')  # Obtener la opción del proveedor (existente o nuevo)

        # Si el usuario eligió un proveedor existente
        if proveedor_id and proveedor_opcion != 'nuevo':
            proveedor_existente = Proveedor.objects.get(pk=proveedor_id)
            Producto.objects.create(nombre=nombre_producto, precio=precio, stock_actual=stock_actual, proveedor=proveedor_existente)
            return redirect('agregar_producto')

        # Si el usuario eligió crear un nuevo proveedor
        elif proveedor_opcion == 'nuevo':
            # Guardar la información del producto en la sesión
            request.session['producto_info'] = {
                'nombre': nombre_producto,
                'precio': precio,
                'stock_actual': stock_actual
            }
            return redirect('agregar_proveedor')

    # Obtener todos los proveedores existentes para mostrar en el formulario
    proveedores = Proveedor.objects.all()

    # Renderizar el formulario de creación de productos con la lista de proveedores
    return render(request, 'productos.html', {'proveedores': proveedores})

def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    messages.success(request, '¡Proveedor eliminado!')
    return redirect('listar_proveedores')


def proveedor_a_actualizar(request, id):
    proveedor = Proveedor.objects.get(id=id)
    return render (request, 'actualizar_proveedor.html', {'proveedor': proveedor})

def actualizar_proveedor(request):
    id = request.POST.get('id')
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    dni = request.POST.get('dni')    

    proveedor = Proveedor.objects.get(id=id)
    proveedor.nombre = nombre
    proveedor.apellido = apellido
    proveedor.dni = dni
    proveedor.save()

    messages.success(request, '¡Proveedor actualizado!')

    return redirect('listar_proveedores')

def inicio(request):
    return render(request, 'inicio.html')