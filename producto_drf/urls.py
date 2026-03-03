from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoDfrViewSet

# Crear un router y registrar el ViewSet
router = DefaultRouter()
router.register(r'productos-drf', ProductoDfrViewSet, basename='producto-drf')

urlpatterns = [
    path('api/', include(router.urls)),
]
