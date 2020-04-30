from django.db import models

# Create your models here.

class User(models.Model): ## Master Table
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now=True,blank=False)
    is_update = models.DateTimeField(auto_now=True,blank=False)


class Employee(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "app/img/")
    gender = models.CharField(max_length=50)