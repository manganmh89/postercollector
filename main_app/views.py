from django.shortcuts import render

from django.http import HttpResponse

class Poster:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, stock, description, printed):
    self.name = name
    self.stock = stock
    self.description = description
    self.printed = printed

posters = [
  Poster('ELO', 'bleached', 'Spaceship, limited print 200', '2019'),
  Poster('Dead & Co', 'foil', 'Washington, DC special print, 50 printed', '2018'),
  Poster('Billy Strings', 'natural', 'Covid couch tour, surfing fox', '2021'),
  Poster("Umphrey's Mcgee", 'bleached', 'Washington DC special, 4 color print', '2017'),
]

#Define the home view
def home(request):
    return HttpResponse('<h1>Hello!</h1>')

def about(request):
    return render(request, 'about.html')

def posters_index(request):
    return render(request, 'posters/index.html', { 'posters': posters })