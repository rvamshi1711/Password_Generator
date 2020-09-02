from django.db import models

# Create your models here.
class GP(models.Model):
    p=models.CharField(max_length=100)
    