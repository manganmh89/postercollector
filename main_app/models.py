from django.db import models

# Create your models here.
class Poster(models.Model):
    band = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    printed = models.IntegerField()

    def __str__(self):
        return self.band
    