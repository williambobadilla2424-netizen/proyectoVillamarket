from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import categoria_producto, usuario, producto, carrito, pedido, pago
from .serializers import categoriaProductoSerializers,usuarioSerialzers,productoSerializers,carritoSerializers,pedidoSerializers,pagoSerializers

class categoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = categoria_producto.objects.all()
    serializer_class = categoriaProductoSerializers

class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerialzers

class productoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = productoSerializers

class carritoViewSet(viewsets.ModelViewSet):
    queryset = carrito.objects.all()
    serializer_class = carritoSerializers

class pedidoViewSet(viewsets.ModelViewSet):
    queryset = pedido.objects.all()
    serializer_class = pedidoSerializers

class pagoViewSet(viewsets.ModelViewSet):
    queryset = pago.objects.all()
    serializer_class = pagoSerializers