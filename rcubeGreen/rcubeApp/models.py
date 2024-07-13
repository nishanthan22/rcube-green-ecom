from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class NewsArticle(models.Model):
    CATEGORY_CHOICES = [
        ('sustainability', 'Sustainability'),
        ('product_review', 'Product Review'),
        ('industry_news', 'Industry News'),
        # Add more categories as needed
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    excerpt = models.TextField(blank=True, null=True)  # Optional short summary
    date_posted = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update this field on save
    image = models.ImageField(upload_to='articles/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='sustainability')
    slug = models.SlugField(unique=True, max_length=255)  # URL-friendly title
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True, blank=True)  # Reference to the user who created the article
    views = models.PositiveIntegerField(default=0)  # Track the number of views
    tags = models.ManyToManyField('Tag', blank=True)  # Tags for the article

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name