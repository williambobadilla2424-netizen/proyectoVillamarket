from django.contrib import admin
from .models import categoria_producto,rol,usuario,producto,carrito,pedido,pago

admin.site.register(categoria_producto)
admin.site.register(rol)
admin.site.register(usuario)
admin.site.register(producto)
admin.site.register(carrito)
admin.site.register(pedido)
admin.site.register(pago)