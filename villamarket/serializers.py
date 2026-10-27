from rest_framework import serializers
from .models import categoria_producto, usuario, producto, carrito, pedido, pago

class categoriaProductoSerializers(serializers.ModelSerializer):
    class META:
        model = categoria_producto
        fields=['id','nombre']

class usuarioSerialzers(serializers.ModelSerializer):
    class META:
        model = usuario
        fields=['id','nombre','correo','password','estado','id_rol']

class productoSerializers(serializers.ModelSerializer):
    class META:
        model = producto
        fileds=['id','nombre','precio','cantidad','id_categoria']

class carritoSerializers(serializers.ModelSerializer):
    class META:
        model = carrito
        fileds=['id','total','id_usuario','id_producto']

class pedidoSerializers(serializers.ModelSerializer):
    class META:
        model = pedido
        fields = ['id','fecha','estado','total','direccion','id_usuario','id_carrito']

class pagoSerializers(serializers.ModelSerializer):
    class META:
        model = pago
        fields = ['id','metodo','estado','fecha','id_pedido']
