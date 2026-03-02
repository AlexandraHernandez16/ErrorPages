from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

"""
URLs para la API REST de Productos usando Django REST Framework
Todas las rutas están bajo el prefijo /api/productos-drf/
"""

# Crear un router y registrar el ViewSet
router = SimpleRouter()
router.register(r'', views.ProductoDfrViewSet, basename='producto-drf')

urlpatterns = [
    path('', include(router.urls)),
]

"""
Rutas disponibles:
- GET    /api/productos-drf/               - Listar todos los productos
- POST   /api/productos-drf/               - Crear un nuevo producto
- GET    /api/productos-drf/<id>/          - Obtener un producto específico
- PUT    /api/productos-drf/<id>/          - Actualizar un producto completo
- PATCH  /api/productos-drf/<id>/          - Actualizar parcialmente un producto
- DELETE /api/productos-drf/<id>/          - Eliminar un producto
- POST   /api/productos-drf/<id>/vender/   - Vender unidades de un producto
- POST   /api/productos-drf/<id>/reabastecer/ - Reabastecer un producto
"""
