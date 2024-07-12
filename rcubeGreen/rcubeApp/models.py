from django.db import models

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
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='sustainability')

    def __str__(self):
        return self.title
