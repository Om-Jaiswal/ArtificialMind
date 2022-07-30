from datetime import date
from django.db import models

# Create your models here.
class ContactForm(models.Model):
    class Meta:
        get_latest_by = "date"
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
    date = models.DateTimeField()