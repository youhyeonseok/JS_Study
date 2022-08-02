from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.EmailField(max_length=64)
    password = models.CharField(max_length=64)
    date = models.DateTimeField()