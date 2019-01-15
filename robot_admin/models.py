from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField('姓名', max_length=100)
    cellphone = models.CharField('电话', max_length=100, unique=True)
    open_id = models.CharField('微信ID', max_length=200, unique=True)
    city = models.CharField('地市', max_length=50, blank=True)
    zone = models.CharField('区县', max_length=50, blank=True)
    department = models.CharField('部门', max_length=200, blank=True)

    def __str__(self):
        return self.name


class QueryLog(models.Model):
    uuid = models.UUIDField('UUID')
    open_id = models.CharField('微信ID', max_length=200)
    url = models.TextField('URL',max_length=6000)
