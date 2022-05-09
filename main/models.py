from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserExtra(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=250)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='image/user', null=True, blank=True)
