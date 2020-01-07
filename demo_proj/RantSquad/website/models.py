from django.db import models

# Create your models here.
class RegisterForm(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=20)
    email = models.TextField()
    password = models.TextField()
