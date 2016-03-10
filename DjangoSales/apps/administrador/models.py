from django.db import models

unidades = (
	("kg","kilogramos"),
	("litros","litros"),
	("cajas","cajas"),
	("piezas","piezas"),
	("paquetes","paquetes"),
	)

class Proveedor(models.Model):

	nombre = models.CharField(max_length=50)
	telefono = models.IntegerField(null=True,blank=True)
	correo = models.EmailField(null=True,blank=True)

	class Meta:
		verbose_name = "Proveedor"
		verbose_name_plural = "Proveedors"

	def __str__(self):
		return self.nombre

class Entradas(models.Model):

	producto = models.CharField(max_length=50)
	proveedor = models.ForeignKey(Proveedor)
	cantidad = models.FloatField(default=0)
	tipo = models.CharField(max_length=50,choices=unidades)
	precio = models.FloatField(default=0)
	fecha = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.producto

class Inventario(models.Model):

	producto = models.CharField(max_length=50)
	proveedor = models.ForeignKey(Proveedor)
	cantidad = models.FloatField(default=0)
	tipo = models.CharField(max_length=50,choices=unidades)
	precio = models.FloatField(default=0)
	fecha = models.DateField(auto_now_add=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.producto
		