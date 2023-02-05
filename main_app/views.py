from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Poster, Dream
from .forms import VariationForm

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
  variation_form = VariationForm()
  toys_cat_doesnt_have= Toy.objects.exclude(id__in)
  return render(request, 'posters/detail.html', { 'poster': poster, 'variation_form' : variation_form })

def add_variation(request, poster_id):
  #capture submitted form inputs
  form = VariationForm(request.POST)
  #validate form inputs
  if form.is_valid():
  #save a temp copy of new variation, using form submission
  #associate new variation to corresponding poster id
  #save new variation to DB
    new_variation = form.save(commit=False)
    new_variation.poster_id = poster_id
    new_variation.save()
  #return with a response to redirect
  return redirect('detail', poster_id=poster_id)
  #import special redirect (built in function)

  def dream_index(request):
    dreams = Dream.objects.all()
    return render(request, 'dreams/index.html', { 'dreams': dreams })

class PosterCreate(CreateView):
  model = Poster
  fields = ('band', 'stock', 'description', 'printed')
  success_url = '/posters/'

class PosterUpdate(UpdateView):
  model = Poster
  fields = ('stock', 'description', 'printed')

class PosterDelete(DeleteView):
  model = Poster
  success_url = '/posters/'

class DreamIndex(ListView):
    model = Dream

class DreamCreate(CreateView):
    model = Dream
    fields = '__all__'

class DreamDetail(DetailView):
    model = Dream

class DreamDelete(DeleteView):
    model = Dream
    success_url = '/dreams/'

class DreamUpdate(UpdateView):
    model = Dream
    fields = '__all__'
