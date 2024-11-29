from django.forms import ModelForm
from .models import *


class bookForm(ModelForm):
    class Meta:
        model = book
        fields = ('name', 'Author', 'price', 'stock', 'image')