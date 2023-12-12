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










####### de aqui para aca abajo es lo que hay que hacer para arquitectura





class Municipalidad(models.Model):
    idMuni = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField(blank=True, null=True)
    url_pag_web = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre




class Pago(models.Model):
    Id_pago = models.IntegerField(blank=True, null=True)  
    fecha_pago = models.DateTimeField(blank = True, null=True)





class adulto_mayor(models.Model):
    Rut = models.IntegerField(blank=True, null=True)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateTimeField(blank = True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=100)




class Instructor(models.Model):
    Rut = models.IntegerField(blank=True, null=True)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=70)
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=100)
    sueldo_base = models.IntegerField(blank=True, null=True)




class Materiales(models.Model):
    Rut = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=30)
    stock = models.IntegerField(blank=True, null=True)




class Talleres(models.Model):
    idtalleres = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)
    horas = models.IntegerField(blank=True, null=True)


class inscripcion(models.Model):
    nombre = models.CharField(max_length=70)
    edad = models.IntegerField(blank=True, null=True)


class Sala(models.Model):
    Idsala = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=70)
    capacidad = models.IntegerField(blank=True, null=True)




class Bono(models.Model):
    Idbono = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=70)
    monto = models.IntegerField(blank=True, null=True)
    frecuencia = models.CharField(max_length=70)



class postulacion_taller(models.Model):
    Idpostulacion = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_termino = models.DateTimeField(blank=True, null=True)
    cupos = models.IntegerField(blank=True, null=True)  
  


###esta nose como se hace asi que hay que revisarla
class Usuario(models.Model):
    Rut = models.IntegerField(blank=True, null=True)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateTimeField(blank = True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=100)
###hasta aqui




class postulacion_instructor(models.Model):
    nro_postulacion = models.IntegerField(blank=True, null=True)
    fecha_postulacion = models.DateTimeField(blank = True, null=True)
    fecha_respuesta = models.DateTimeField(blank = True, null=True)
    #aqui en la base de datos sale certificados con archivos blob
    puntaje_total = models.IntegerField(blank=True, null=True)
    aceptado = models.CharField(max_length=30)##aca ponerlo en char




class Credencial(models.Model):
    id_credencial = models.IntegerField(blank=True, null=True)
    nombre_usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)





    




    
    




    

    



 





