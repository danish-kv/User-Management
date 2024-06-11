from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=150)
    phone = models.IntegerField()
    password = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='meadia', blank=True, null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.username