from django.db import models

class rol(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class categoria_producto(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    estado = models.BooleanField()
    id_rol = models.ForeignKey(rol,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    id_categoria = models.ForeignKey(categoria_producto,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class carrito(models.Model):
    total = models.FloatField()
    id_usuario = models.ForeignKey(usuario,on_delete=models.CASCADE)
    id_producto = models.ForeignKey(producto,on_delete=models.CASCADE)

    def __str__(self):
        return self.total

class pedido(models.Model):
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=100)
    total = models.IntegerField()
    direccion = models.CharField(max_length=20)
    id_usuario = models.ForeignKey(usuario,on_delete=models.CASCADE)
    id_carrito = models.ForeignKey(carrito,on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha

class pago(models.Model):
    metodo = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    id_pedido = models.ForeignKey(pedido,on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha