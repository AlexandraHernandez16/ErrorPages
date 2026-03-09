from rest_framework import serializers
from .models import productoDfr


class ProductoDfrSerializer(serializers.ModelSerializer):
    # Campos virtuales, de apoyo
    foto_para_binario = serializers.ImageField(write_only=True, required=False)
    foto_base64_display = serializers.ReadOnlyField(source='foto_base64')

    class Meta:
        model = productoDfr
        fields = [
            'id', 'nombre', 'precio', 'stock', 'categoria', 'descripcion',
            'fecha_creacion', 'fecha_actualizacion', 'foto', 'foto_para_binario', 'foto_base64_display'
        ]

    def create(self, validated_data):
        # Extraemos el segundo archivo (el que va a la base de datos), es nulo si no lo mandaron
        archivo_binario = validated_data.pop('foto_para_binario', None)

        # DRF guarda 'foto' automáticamente en la carpeta /media/
        producto = productoDfr.objects.create(**validated_data)

        # Si nos mandaron el segundo archivo, leemos sus bytes crudos y los guardamos
        if archivo_binario:
            # .read() extrae los bytes del archivo, ¡no se necesita base64 aquí!
            producto.foto_binaria = archivo_binario.read()
            producto.save()

        return producto

    def update(self, instance, validated_data):
        # Extraemos el segundo archivo (el que va a la base de datos), es nulo si no lo mandaron
        archivo_binario = validated_data.pop('foto_para_binario', None)

        # Actualizamos los campos normales
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Si nos mandaron un nuevo archivo binario, lo guardamos
        if archivo_binario:
            instance.foto_binaria = archivo_binario.read()

        instance.save()
        return instance