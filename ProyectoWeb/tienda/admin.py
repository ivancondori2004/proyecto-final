from django.contrib import admin
from .models import CategoriaProd, Producto, Proveedor, Producto, Empleado, OrdenCompra

# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

class ProductoAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")
    list_display=('nombre','categorias','contenido','precio')
    list_fields=('nombre','categorias','contenido','precio')
    list_filter=('categorias',) 

# nuevo

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=('id_emp','nombre_emp','apellido_emp','telefono_emp','email_emp','cargo_emp')
    list_fields=('nombre_emp','apellido_emp','cargo_emp')
    list_filter=('cargo_emp',)

class ProveedorAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','telefono_provee','plazo_entrega')
    list_fields=('nombre','apellido','telefono_provee','plazo_entrega')
    list_filter=('plazo_entrega',)
    
class OrdenCompraAdmin(admin.ModelAdmin):
    list_display=('proveedor','empleado','fecha_orden')
    list_fields=('proveedor','empleado','fecha_orden')
    list_filter=('fecha_orden',)
    list_display=('producto','cantidad')
    list_fields=('producto','cantidad') 
    date_hierarchy='fecha_orden'
    
    
class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display=('producto','cantidad')
    list_fields=('producto','cantidad') 
    


admin.site.register(CategoriaProd, CategoriaProdAdmin)

admin.site.register(Producto, ProductoAdmin)

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(OrdenCompra, OrdenCompraAdmin)
