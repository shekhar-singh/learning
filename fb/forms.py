from django import forms

from .models import Join

class EmailForm(forms.ModelForm):
	passwrd = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Join
		fields = ['email', 'passwrd','name']


