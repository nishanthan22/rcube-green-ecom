from django import forms
from .models import GreenInnovation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
import re


def alphanumeric_validator(value):
    if not re.match(r'^[a-zA-Z\s]*$', value):
        raise ValidationError('This field should only contain letters and spaces, with no special characters or numbers.')

class GreenInnovationForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('GreenInnovation', 'Green Innovation'),
        ('EcoProducts', 'Eco Products'),
        ('SustainableLiving', 'Sustainable Living'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Category')

    class Meta:
        model = GreenInnovation
        fields = ['title', 'slug', 'author', 'category', 'content','status', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'required': 'required'}),
            'slug': forms.TextInput(attrs={'required': 'required'}),
            'author': forms.TextInput(attrs={'required': 'required'}),
            'content': forms.Textarea(attrs={'required': 'required'}),
            'status': forms.Select(attrs={'required': 'required'}),
            'image': forms.FileInput(attrs={'required': 'required'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Append the custom validator to the fields
        self.fields['title'].validators.append(alphanumeric_validator)
        self.fields['slug'].validators.append(alphanumeric_validator)
        self.fields['author'].validators.append(alphanumeric_validator)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        alphanumeric_validator(title)
        return title

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        alphanumeric_validator(slug)
        return slug

    def clean_author(self):
        author = self.cleaned_data.get('author')
        alphanumeric_validator(author)
        return author