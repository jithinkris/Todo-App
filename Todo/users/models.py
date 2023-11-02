from django.db import models

# Create your models here.


class User(models.Model):
    Name=models.CharField(max_length=30)
    Phone=models.CharField(max_length=10,primary_key=True)
    Password=models.CharField(max_length=16)

class Todolist(models.Model):
    phone=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    desc=models.CharField(max_length=80)
    duedate=models.DateField()
    status=models.IntegerField()

