from django.db import models

class Join(models.Model):
	email=models.EmailField(unique=True, blank=False)
	passwrd=models.CharField(max_length=200)
	name=models.CharField(max_length=200)

	def __unicode__(self):
		return self.email


