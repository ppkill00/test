from django.db import models

# Create your models here.

class Alert(models.Model):
    server = models.CharField(max_length=30)
    message = models.CharField(max_length=30)