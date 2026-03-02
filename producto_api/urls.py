from django.urls import path
from . import views

"""
URLs para la API de Productos
Todas las rutas están bajo el prefijo /api/productos/
"""

urlpatterns = [
    # READ - Listar todos los productos
    # GET /api/productos/
    path('', views.api_lista_productos, name='api_lista_productos'),
    
    # CREATE - Crear un nuevo producto
    # POST /api/productos/crear/
    path('crear/', views.api_crear_producto, name='api_crear_producto'),
    
    # UPDATE - Actualizar un producto existente
    # PUT /api/productos/actualizar/<id>/
    path('actualizar/<int:pk>/', views.api_actualizar_producto, name='api_actualizar_producto'),
    
    # DELETE - Eliminar un producto
    # DELETE /api/productos/eliminar/<id>/
    path('eliminar/<int:pk>/', views.api_eliminar_producto, name='api_eliminar_producto'),
]
