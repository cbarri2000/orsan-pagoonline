from django.db import models

class Usuario(models.Model):
	rut = models.CharField(max_length=8)
	dvrut = models.CharField(max_length=1)
	mail = models.CharField(max_length=100)
	clave = models.CharField(max_length=20)
	nombre = models.CharField(max_length=100)
	direccion = models.CharField(max_length=100)
	telefono = models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre