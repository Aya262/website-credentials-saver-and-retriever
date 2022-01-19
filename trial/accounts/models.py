from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db.models.base import Model
from . manager import CustomUserManager
# Create your models here.


class CustomUser(AbstractBaseUser,PermissionsMixin):
    use_in_migrations=True
    email=models.EmailField(max_length=254,unique=True)
    name=models.CharField(max_length=30)
    secondEmail=models.EmailField(max_length=254,null=True,blank=True)
    password=models.CharField(max_length=30)
    phone=models.IntegerField(null=True,blank=True)
    secondPhone=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    question=models.CharField(max_length=50,null=True,blank=True)
    answer=models.CharField(max_length=50,null=True,blank=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name','secondEmail','password','phone']

    objects=CustomUserManager()

    def __str__(self):
        return self.email




class websites(models.Model):
    userID=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    recoveremail=models.EmailField(max_length=254,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

