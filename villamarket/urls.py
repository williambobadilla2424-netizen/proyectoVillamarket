from django.urls import path,include
from .views import categoriaProductoViewSet,usuarioViewSet,productoViewSet,pedidoViewSet,carritoViewSet,pagoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categoriaProductos', categoriaProductoViewSet, basename='categoriaProductos')
router.register('usuarios', usuarioViewSet, basename='usuarios')
router.register('productos', productoViewSet, basename='productos')
router.register('carrito', carritoViewSet, basename='carrito')
router.register('pedidos', pedidoViewSet,basename='pedidos')
router.register('pagos',pagoViewSet, basename='pagos')

urlpatterns = [
    path('', include(router.urls))
]