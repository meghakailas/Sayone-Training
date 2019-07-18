from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
class UserProfileInfo(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='userprofile')

	mobile = models.IntegerField()
	
	def __str__(self):
  		return self.user.username

  	