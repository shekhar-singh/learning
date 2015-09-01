from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import Join

class EmailForm(forms.ModelForm):
	passwrd = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Join
		fields = ['email', 'passwrd','name']

class LoginForm(forms.Form):
	email = forms.CharField(max_length=120)
	passwrd = forms.CharField(widget=forms.PasswordInput()) 


class ProfileForm(forms.Form):
	BIRTH_YEAR_CHOICES = ('1980', '1981', '1982','1983','1984','1985','1986','1987','1988','1989','1990')
    Title_Choice = ((1, _("Mr.")),(2, _("Ms.")),)
	DOB=forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
	#title = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices=Title_Choice)
	age = forms.IntegerField()
    nationality = forms.CharField()