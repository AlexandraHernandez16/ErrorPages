from rest_framework import viewsets
from .models import productoDfr
from .serializers import ProductoDfrSerializer


class ProductoDfrViewSet(viewsets.ModelViewSet):
    """
    ViewSet para operaciones CRUD de Productos usando Django REST Framework
    
    Endpoints disponibles:
    - GET /api/productos-drf/               - Listar todos los productos
    - POST /api/productos-drf/              - Crear un nuevo producto
    - GET /api/productos-drf/<id>/          - Obtener un producto específico
    - PUT /api/productos-drf/<id>/          - Actualizar un producto completo
    - PATCH /api/productos-drf/<id>/        - Actualizar parcialmente un producto
    - DELETE /api/productos-drf/<id>/       - Eliminar un producto
    """
    
    queryset = productoDfr.objects.all()
    serializer_class = ProductoDfrSerializer
