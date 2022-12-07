from django.db import models

# Create your models here.
class tblInventario(models.Model):
    id_producto=models.CharField(max_length=3, null=True)
    nombre=models.CharField(max_length=50, null=True)
    unidad=models.IntegerField(default='0')
    precio=models.CharField(max_length=4, null=True)
    cantidad=models.CharField(max_length=4, null=True)
    existencias=models.IntegerField(default='0')
    

    def __str__(self):
        return str(self.nombre)

class tblPasteleria(models.Model):
    id_sucursal=models.CharField(max_length=3, null=True)
    nombre=models.CharField(max_length=50, null=True)
    descripcion=models.TextField()
    existencias=models.ForeignKey(tblInventario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)   

class tblEmpleados(models.Model):
    id_empleado=models.CharField(max_length=4, null=True)
    nombre=models.CharField(max_length=50, null=True)
    apellido=models.CharField(max_length=50, null=True)
    cargo=models.CharField(max_length=6, null=True)

    def __str__(self):
        return str(self.nombre)

class tblProveedores(models.Model):
    id_proveedor=models.CharField(max_length=3, null=True)
    nombre=models.CharField(max_length=50, null=True)
    apellido=models.CharField(max_length=50, null=True)
    telefono=models.CharField(max_length=8, null=True)
    cantidad=models.ForeignKey(tblInventario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)

class tblClientes(models.Model):
    id_cliente=models.CharField(max_length=10, null=True)
    nombre=models.CharField(max_length=50, null=True)
    apellido=models.CharField(max_length=50, null=True)
    factura=models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.nombre)
    

class tblEncargos(models.Model):
    id_encargo=models.CharField(max_length=3, null=True)
    anticipo=models.CharField(max_length=5, null=True)
    fecha_encargo=models.DateField()
    fecha_entrega=models.DateField()
    factura=models.ForeignKey(tblClientes, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_encargo)