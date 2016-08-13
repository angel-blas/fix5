from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post, Categoria
from .forms import PostForm, CommForm
from django.utils.text import slugify

from django.utils.decorators import method_decorator #nos deja usar decorador
from django.contrib.auth.decorators import login_required #es el decorador


class ListView(View):
	def get(self,request,cat=None):#Categoria puede o no estar, por eso se pone none
		template_name = 'lista.html'
		#Esta variable es una auxiliar para saber si está mostrando las categorias o está mostrando todos
		categoria=None
		if cat:
			categoria=Categoria.objects.get(nombre=cat)
			posts=categoria.posts.all()
		else:
			posts = Post.objects.all().order_by('-fecha')
		context = {
		'posts':posts,
		'categoria':categoria
		}
		return render(request,template_name,context)



class DetailView(View):
	def get(self,request,slug):#cambiar slug
		template_name='detalle.html'
		#post=Post.objects.get(pk=id)
		post=Post.objects.get(slug=slug)

		comentarios=post.comentarios.all()#aquí agregamos esto para mostrar los comentarios
		form=CommForm()
		context = {
		'post':post,
		'comments':comentarios,
		'form':form}
		return render(request,template_name,context)

	def post(self, request, slug):
		form=CommForm(request.POST)
		
		post=Post.objects.get(slug=slug)
		new_comm=form.save(commit=False)
		new_comm.user=request.user
		new_comm.post=post
		new_comm.save()
		return redirect('detalle', slug=slug)




class UpdateView(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'nuevo.html'
		form = PostForm()
		context = {
		'form':form,
		}
		return render(request, template_name,context)

	def post(self,request):
		form = PostForm(request.POST)
		new_post = form.save(commit=False)
		new_post.slug = slugify(new_post.titulo)
		new_post.save()
		return redirect('lista')


# Create your views here.
