from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.
class Poster(models.Model):
    band = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    printed = models.IntegerField()

    def __str__(self):
        return self.band

    def get_absolute_url(self):
        return reverse('detail', kwargs={'poster_id': self.id})

class Variation(models.Model):
    OPTIONS = (
        ('F', 'Foil'),
        ('B', 'Bleached'),
        ('N', 'Natural'),
        ('C', 'Color'),
    )
    date = models.DateField('date printed')
    option = models.CharField(max_length=1, choices=OPTIONS, default=OPTIONS[0][0])
    poster = models.ForeignKey(Poster, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_option_display()} on {self.date}"