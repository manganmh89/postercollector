from django.contrib import admin

#import you models here
from .models import Poster, Variation

# Register your models here.
admin.site.register(Poster)

admin.site.register(Variation)