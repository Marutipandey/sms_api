from django.db import models

class SMS(models.Model):
    to_number = models.CharField(max_length=15)
    message = models.TextField()
