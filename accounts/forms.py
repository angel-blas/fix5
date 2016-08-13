from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
	password = forms.CharField(label = 'Tu Password nuevo',widget=forms.PasswordInput)
	password2 = forms.CharField(label = 'Repite tu pasword', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username','first_name','email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password']!= cd['password2']:
			raise forms.ValidationError('Tus passwords no coinciden compa')
		return cd['password2']