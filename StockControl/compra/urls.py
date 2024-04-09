from django.urls import path
from . import views 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/crear_producto/', views.agregar_producto, name='agregar_producto'),
    path('productos/listar_productos/', views.listar_productos, name='listar_productos'),
    path('productos/listar_productos/eliminar_producto/<id>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/listar_productos/producto_a_actualizar/<id>/', views.producto_a_actualizar, name='productos_a_actualizar'),
    path('productos/listar_productos/actualizar_producto/', views.actualizar_producto, name='actualizar_producto'),
    path('proveedores/', views.listar_proveedores , name= 'listar_proveedores'),
    path('proveedores/crear_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/eliminar_proveedor/<id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('proveedores/proveedor_a_actualizar/<id>/', views.proveedor_a_actualizar, name='proveedor_a_actualizar'),
    path('proveedores/actualizar_proveedor/', views.actualizar_proveedor, name='actualizar_proveedor'),

]