from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=50)

# class register(models.Model):
#     fname=models.CharField(max_length=20)
#     eml=models.CharField(max_length=10)
#     psw=models.IntegerField(max_length=5)


