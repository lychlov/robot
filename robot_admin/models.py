from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=100)
    open_id = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
