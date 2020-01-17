from django.db import models

# Create your models here.

class AddincomeModel(models.Model):
    date=models.DateField()
    text=models.CharField(max_length=50)
    amount=models.DecimalField(max_digits=50,decimal_places=2)


class AddexpenseModel(models.Model):
    date=models.DateField()
    text=models.CharField(max_length=50)
    amount=models.DecimalField(max_digits=50,decimal_places=2)
