from django import forms

from .models import Join

class EmailForm(forms.ModelForm):
	passwrd = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Join
		fields = ['email', 'passwrd','name']

class LoginForm(forms.Form):
	email = forms.CharField(max_length=120)
	passwrd = forms.CharField(widget=forms.PasswordInput()) 


