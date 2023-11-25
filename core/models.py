from django.db import models




class TipoProducto(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True)
    agregados = models.CharField(max_length=150, blank=True)
    precio_agregados = models.IntegerField(blank=True, null=True)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    disponible = models.BooleanField()

    def __str__(self):
        return self.nombre
    

class ContactForm(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=100)    
    fecha = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre