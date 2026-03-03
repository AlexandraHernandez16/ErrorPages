from django.db import models

class productoDfr(models.Model):
    
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    precio = models.FloatField(verbose_name="Precio")
    stock = models.IntegerField(default=0, verbose_name="Stock Disponible")
    categoria = models.CharField(max_length=100, verbose_name="Categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

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
