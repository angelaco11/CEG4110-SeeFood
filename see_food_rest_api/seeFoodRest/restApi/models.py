from django.db import models

# Create your models here.

class ProcessedImage(models.Model):
    file_path = models.CharField(max_length=100)
    upper = models.FloatField()
    lower = models.FloatField()
    upload_date = models.DateTimeField()
