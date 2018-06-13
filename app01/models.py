from django.db import models

# Create your models here.

class Publisher(models.Model):
    id=models.AutoField(primary_key=True)#主键自增
    pname=models.CharField(max_length=64)#varchar(64)

class Book(models.Model):
    id=models.AutoField(primary_key=True)#主键自增
    bname=models.CharField(max_length=64)
    publisher=models.ForeignKey(to=Publisher)


