from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.decorators import method_decorator #nos deja usar decorador
from django.contrib.auth.decorators import login_required #es el decorador
from .forms import RegistrationForm
from .models import Perfil



# Create your views here.

class PerfilView(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'accounts/perfil.html'
		context = {}
		return render (request,template_name,context)

class Alta(View):
	def get(self, request):
		template_name = 'accounts/alta.html'
		form = RegistrationForm()
		context ={
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		form=RegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)#si no se pone commit, se guarda, así que le ponemos false para no guardarlo hasta después
			new_user.set_password(form.cleaned_data['password'])#hashea el password 24000 veces
			new_user.save()#se guardan los datos
			#Aquí se le asigna un perfil a un usuario
			perfil_nuevo=Perfil()
			perfil_nuevo.user=new_user
			perfil_nuevo.save()
			return redirect('perfil')#en lugar de renderizar aquí mismo nos manda a otra vista

		else:
			context = {
			'form':form,}
			template_name='accounts/alta.html'
			return render(request,template_name,context)