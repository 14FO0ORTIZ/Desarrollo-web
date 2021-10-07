from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Cliente(models.Model):
    doc = (
     ("D","DPI"),
     ("C","CEDULA"),
    )
   
    nombre=models.CharField(max_length=50) 
    apellido=models.CharField(max_length=50) 
    direccion=models.CharField(max_length=200) 
    nacimineto=models.DateField()
    tipo = models.ForeignKey(
       'TipoCliente',
        on_delete= models.CASCADE,
        default=1
    )
    documento=models.CharField(
        max_length=20,
        choices=doc,
        default="C")  
    creacion=models.DateField(auto_now_add=True)
    actulizacion=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)


class TipoCliente(models.Model):
   
    tipo=models.CharField(max_length=50) 
    creacion=models.DateField(auto_now_add=True)
    actulizacion=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return '%s' % (self.tipo)

class venta(models.Model):
    cliente = models.ManyToManyField(Cliente)
    fecha = models.DateTimeField()

    def __str__(self):
        return '%s %s' % (self.cliente,self.fecha)

class Estudiante(models.Model):
   
    nombre=models.CharField(max_length=50) 
    apellido=models.CharField(max_length=50) 
    direccion=models.CharField(max_length=200) 
    imagen = models.CharField(max_length=500,default=" ")

    def __str__(self):
        return '%s %s %s' % (self.nombre,self.apellido,self.direccion)


