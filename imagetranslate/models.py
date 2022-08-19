from django.db import models

# Create your models here.
class MultipleImage(models.Model):
    images = models.FileField()
    lang = models.CharField(default="English", max_length=1000000)