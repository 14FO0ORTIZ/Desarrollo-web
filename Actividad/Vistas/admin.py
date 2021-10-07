from django.contrib import admin
from .models import Cliente, Estudiante,TipoCliente,venta
# Register your models here.
admin.site.register( Cliente)
admin.site.register( TipoCliente)
admin.site.register( venta)
admin.site.register( Estudiante)





