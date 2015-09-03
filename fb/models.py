from django.db import models
#from django.contrib.auth.models import User

class Join(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField(unique=True, blank=False)
	passwrd=models.CharField(max_length=200)
	

	def __unicode__(self):
		return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(Join, unique=True)
    home_address = models.TextField(null=True,blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    
    def __unicode__(self):
    	return self.user

