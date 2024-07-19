from django import forms
from .models import GreenInnovation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

class GreenInnovationForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('GreenInnovation', 'Green Innovation'),
        ('EcoProducts', 'Eco Products'),
        ('SustainableLiving', 'Sustainable Living'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Category')

    class Meta:
        model = GreenInnovation
        fields = ['title', 'slug', 'author', 'category', 'content', 'status', 'image']
