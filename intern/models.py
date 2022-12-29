from django.db import models


# Create your models here.

class PostHouse(models.Model):
    name = models.CharField(max_length=30)
    phno = models.TextField()
    housename = models.TextField()
    houseno = models.TextField()
    houseaddr = models.TextField()
    houseimg = models.ImageField(upload_to='pics')
    description = models.TextField()
