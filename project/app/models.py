from django.db import models

# Create your models here.
class todo(models.Model):
    date=models.DateField()
    list=models.TextField()