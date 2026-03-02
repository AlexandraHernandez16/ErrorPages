from rest_framework import serializers
from .models import productoDfr


class ProductoDfrSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo productoDfr
    Convierte instancias del modelo a/desde JSON
    """
    
    class Meta:
        model = productoDfr
        fields = [
            'id', 
            'nombre', 
            'precio', 
            'stock', 
            'categoria', 
            'descripcion',
            'fecha_creacion',
            'fecha_actualizacion'
        ]
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']
