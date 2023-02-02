from django.forms import ModelForm
from .models import Variation

class VariationForm(ModelForm):
    class Meta:
        model = Variation
        fields = ['date', 'option']
