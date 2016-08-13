from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User #Recordar este para todala vida!!!!

#User es un modelo de django que ya hizo así que lo debemos traer

class Post(models.Model):
	titulo = models.CharField(max_length=140)
	fecha = models.DateTimeField(auto_now=True)
	cuerpo = models.TextField()
	publicado = models.BooleanField(default=False)
	slug = models.SlugField(max_length=500,blank=True,null=True)#Modelo Slug

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('detalle',args=[self.slug])


class Comentario(models.Model):
	user= models.ForeignKey(User,related_name='comentarios') #Relación uno a muchos
	fecha = models.DateTimeField(auto_now=True)
	cuerpo = models.TextField()
	post = models.ForeignKey(Post, related_name='comentarios')

	def __str__(self):
		return 'Este comentario lo hizo {} en el post {}'.format(self.user,self.post)


class Categoria(models.Model):
	nombre=models.CharField(max_length=140)
	posts=models.ManyToManyField(Post, related_name='categorias')#Entramos desde post hasta categorías

	def __str__(self):
		return self.nombre
