from django.db import models
import uuid
# Create your models here.
class Webpage(models.Model):
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=200,default='men')
    photo=models.CharField(max_length=2080)
    description=models.TextField()


class Content(models.Model):
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=200,default='men')
    pic=models.CharField(max_length=2080)
    des=models.TextField()
    rate=models.FloatField()
    link=models.CharField(max_length=2080)
    SearchableFields= ['name'] 

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    type=models.CharField(max_length=200)
    message=models.TextField()


class User(models.Model):
    name=models.CharField(max_length=2080)
    password=models.CharField(max_length=200)
    products=models.TextField(default='9999')
