from django.shortcuts import render
from .models import Poster

# class Poster:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, band, stock, description, printed):
#     self.band = band
#     self.stock = stock
#     self.description = description
#     self.printed = printed

# posters = [
#   Poster('ELO', 'bleached', 'Spaceship, limited print 200', '2019'),
#   Poster('Dead & Co', 'foil', 'Washington, DC special print, 50 printed', '2018'),
#   Poster('Billy Strings', 'natural', 'Covid couch tour, surfing fox', '2021'),
#   Poster("Umphrey's Mcgee", 'bleached', 'Washington DC special, 4 color print', '2017'),
# ]

#Define the home view
def home(request):
    return render(request, 'home.html')

def admin(request):
    return render(request, 'admin.html')

def about(request):
    return render(request, 'about.html')

def posters_index(request):
    posters = Poster.objects.all()
    return render(request, 'posters/index.html', { 'posters': posters })

def posters_detail(request, poster_id):
  poster = Poster.objects.get(id=poster_id)
  return render(request, 'posters/detail.html', { 'poster': poster })