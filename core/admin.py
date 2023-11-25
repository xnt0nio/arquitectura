from django.contrib import admin
from .models import *

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','descripcion','tipo','disponible']
    search_fields = ['nombre']
    list_per_page = 10
    list_filter = ['tipo','precio']
    list_editable = ['precio','descripcion','tipo','disponible']


admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)