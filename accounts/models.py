from django.db import models
from django.contrib.auth.models import User#ya está creado por django

# Create your models here.

class Perfil(models.Model):
	GENEROS = (
		('Hombre','Hombre'),
		('Mujer','Mujer'),
	)
	fecha_nacimiento = models.DateField(null=True, blank=True)
	ocupacion = models.CharField(max_length=140, null=True, blank=True)
	sexo = models.CharField(max_length=140, choices=GENEROS, default="Mujer")
	bio = models.TextField(null=True, blank=True)
	#Relación de usuarios con perfil
	user = models.OneToOneField(User)

	def __str__(self):
		return 'este perfil le pertenece a {}'.format(self.user)