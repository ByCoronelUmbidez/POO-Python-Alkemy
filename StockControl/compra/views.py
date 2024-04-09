from django.shortcuts import render, redirect
from .models import Producto
from .models import Proveedor
from django.contrib import messages


def listar_productos(request):
    productos = Producto.objects.all()
    return render (request, 'listar_productos.html', {'productos': productos})

def listar_proveedores(request):
    proveedor = Proveedor.objects.all()
    return render (request, 'listar_proveedores.html', {'proveedor': proveedor})

def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        
        # Verificamos si hay información de producto en la sesión
        if 'producto_info' in request.session:
            # Si hay información de producto, creamos el proveedor pero no lo redirigimos
            Proveedor.objects.create(nombre=nombre, apellido=apellido, dni=dni)
            # Obtenemos la información del producto de la sesión
            producto_info = request.session.pop('producto_info')
            # Creamos el producto con el nuevo proveedor
            proveedor_nuevo = Proveedor.objects.get(nombre=nombre, apellido=apellido, dni=dni)
            Producto.objects.create(nombre=producto_info['nombre'], precio=producto_info['precio'], stock_actual=producto_info['stock_actual'], proveedor=proveedor_nuevo)
            # Redirigimos al usuario a la página de listar proveedores
            return redirect('listar_proveedores')
        
        else:
            # Si no hay información de producto, creamos el proveedor y redirigimos al usuario a la página de listar proveedores
            Proveedor.objects.create(nombre=nombre, apellido=apellido, dni=dni)
            return redirect('listar_proveedores')
    
    return render(request, 'nuevo_proveedor.html') 

def agregar_producto(request):
    if request.method == 'POST':
        nombre_producto = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock_actual = request.POST.get('stock_actual')
        proveedor_id = request.POST.get('proveedor_id')
        proveedor_opcion = request.POST.get('proveedor_seleccionado')

        # Si el usuario elige crear un nuevo proveedor y no ha seleccionado uno existente del desplegable
        if proveedor_opcion == 'nuevo':
            # Guardamos temporalmente la información del producto en la sesión
            request.session['producto_info'] = {
                'nombre': nombre_producto,
                'precio': precio,
                'stock_actual': stock_actual
            }
            # Redirigimos al usuario a la vista agregar_proveedor
            return redirect('agregar_proveedor')

        # Si el usuario elige un proveedor existente
        elif proveedor_id:
            # Obtenemos el proveedor seleccionado
            proveedor_existente = Proveedor.objects.get(pk=proveedor_id)
            # Creamos el producto y lo asociamos con el proveedor existente
            Producto.objects.create(nombre=nombre_producto, precio=precio, stock_actual=stock_actual, proveedor=proveedor_existente)
            # Redirigimos al usuario a la página de listar productos
            return redirect('listar_productos')

    proveedores = Proveedor.objects.all()
    return render(request, 'nuevo_producto.html', {'proveedores': proveedores})

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

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    messages.success(request, 'Producto eliminado!')
    return redirect('listar_productos')


def producto_a_actualizar(request, id):
    producto = Producto.objects.get(id=id)
    return render (request, 'actualizar_producto.html', {'producto': producto})

def actualizar_producto(request):
    id = request.POST.get('id')
    nombre = request.POST.get('nombre')
    precio = request.POST.get('precio')
    stock_actual = request.POST.get('stock_actual')
    proveedor_id = request.POST.get('proveedor_id')      

    producto = Producto.objects.get(id=id)
    producto.nombre = nombre
    producto.precio = precio
    producto.stock_actual = stock_actual
    producto.proveedor_id = proveedor_id
    producto.save()

    messages.success(request, '¡Producto actualizado!')

    return redirect('listar_productos')

def inicio(request):
    return render(request, 'inicio.html')