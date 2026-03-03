from rest_framework import viewsets
from .models import productoDfr
from .serializers import ProductoDfrSerializer


class ProductoDfrViewSet(viewsets.ModelViewSet):
    queryset = productoDfr.objects.all()
    serializer_class = ProductoDfrSerializer
