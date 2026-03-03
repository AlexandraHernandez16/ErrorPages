from rest_framework import serializers
from .models import productoDfr


class ProductoDfrSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = productoDfr
        fields = '__all__'
