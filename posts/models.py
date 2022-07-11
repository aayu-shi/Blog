from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title=models.CharField( max_length=100, default="")
    details=models.CharField(default="", max_length=10000)
    created_on=models.DateTimeField(default=datetime.now,blank=True)