from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    employee_id = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile',null=True, blank=True)
    username = models.CharField(max_length=100 , null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True , null=True , blank=True)
    userImage = models.ImageField(upload_to='profile',null=True,default='/default/githubProfile.jpg')
    bio = models.TextField(max_length=500 , null=True, blank=True , default='this is my bio ')

    def __str__(self):
        return self.username