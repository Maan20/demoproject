from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 200)
    marks = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 200)