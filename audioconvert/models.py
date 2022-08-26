from django.db import models

# Create your models here.
class MultipleAudio(models.Model):
    images = models.FileField()
    ilang = models.CharField(default="English", max_length=1000000)
    tlang = models.CharField(default="English", max_length=1000000)