from rest_framework import serializers
from .models import rol, categoria_producto, usuario, producto, carrito, pedido, pago

class rolSerializers(serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = ['id','nombre']

class categoriaProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = categoria_producto
        fields=['id','nombre']

class usuarioSerialzers(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields=['id','nombre','correo','password','estado','id_rol']

class productoSerializers(serializers.ModelSerializer):
    class Meta:
        model = producto
        fileds=['id','nombre','precio','cantidad','id_categoria']

class carritoSerializers(serializers.ModelSerializer):
    class Meta:
        model = carrito
        fileds=['id','total','id_usuario','id_producto']

class pedidoSerializers(serializers.ModelSerializer):
    class Meta:
        model = pedido
        fields = ['id','fecha','estado','total','direccion','id_usuario','id_carrito']

class pagoSerializers(serializers.ModelSerializer):
    class Meta:
        model = pago
        fields = ['id','metodo','estado','fecha','id_pedido']
