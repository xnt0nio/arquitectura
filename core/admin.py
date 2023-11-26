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


admin.site.register(pago)
admin.site.register(adulto_mayor)
admin.site.register(instructor)
admin.site.register(Materiales)
admin.site.register(Talleres)
admin.site.register(Sala)
admin.site.register(bono)
admin.site.register(postulacion_taller)
admin.site.register(usuario)
admin.site.register(postulacion_instructor)
admin.site.register(credencial)