from django.contrib import admin
from .models import tblPasteleria, tblInventario, tblClientes, tblEmpleados, tblEncargos, tblProveedores
# Register your models here.

admin.site.register(tblEncargos)
admin.site.register(tblPasteleria)
admin.site.register(tblInventario)
admin.site.register(tblClientes)
admin.site.register(tblEmpleados)
admin.site.register(tblProveedores)