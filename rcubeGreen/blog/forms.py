# forms.py
from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author_name', 'category', 'content', 'cover_image']
        widgets = {
            'content': forms.Textarea(attrs={'id': 'id_content'}),
        }
