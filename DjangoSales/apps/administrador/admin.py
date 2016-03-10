from django.contrib import admin

from .models import (
	Proveedor,
	Entradas,
	Inventario
	)

admin.site.register(Proveedor)
admin.site.register(Entradas)
admin.site.register(Inventario)
