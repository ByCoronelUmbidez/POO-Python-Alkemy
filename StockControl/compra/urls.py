from django.urls import path
from . import views 

urlpatterns = [
    path('', views.inicio),
    path('productos/', views.listar_productos, name= 'productos' ),
    path('crear_producto/', views.agregar_producto, name='agregar_producto'),
    path('proveedores/', views.listar_proveedores , name= 'listar_proveedores'),
    path('crear_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/eliminar_proveedor/<id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('proveedores/proveedor_a_actualizar/<id>/', views.proveedor_a_actualizar, name='proveedor_a_actualizar'),
    path('proveedores/actualizar_proveedor/', views.actualizar_proveedor, name='actualizar_proveedor'),

]