from django.db import models
# Import the reverse function
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Dream(models.Model):
    band = models.CharField(max_length=50)
    stock = models.CharField(max_length=20)
    tour = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.band} {self.tour}, {self.year} {self.stock}'

    def get_absolute_url(self):
        return reverse('dream_detail', kwargs={'pk': self.id})

class Poster(models.Model):
    band = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    printed = models.IntegerField()
    dream = models.ManyToManyField(Dream)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def print_for_today(self):
        return self.variation_set.filter(date=date.today()).count() >= len(OPTION)

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

    class Meta:
        ordering = ['-date']

