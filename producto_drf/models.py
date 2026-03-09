import base64

from django.db import models

class productoDfr(models.Model):
    
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    precio = models.FloatField(verbose_name="Precio")
    stock = models.IntegerField(default=0, verbose_name="Stock Disponible")
    categoria = models.CharField(max_length=100, verbose_name="Categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    # CAMPO PARA GUARDAR LA IMAGEN EN EL BACK
    # upload_to='productos/' creará una carpeta llamada "productos" dentro de tu directorio "media"
    foto = models.ImageField(upload_to='productos/', blank=True, null=True)

    # CAMPO BINARIO PARA LA IMAGEN EN LA BD
    foto_binaria = models.BinaryField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    @property
    def foto_base64(self):
        if self.foto_binaria:
            # Convierte los bytes a un string codificado en base64
            codificado = base64.b64encode(self.foto_binaria).decode('utf-8')
            return f"data:image/jpeg;base64,{codificado}"
        return None

    def vender(self, cantidad=1):
        if self.stock >= cantidad:
            self.stock -= cantidad
            self.save()
            return True
        return False

    def reabastecer(self, cantidad=1):
        self.stock += cantidad
        self.save()
        return True
