from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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


class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateTimeField(default=timezone.now)
    method = models.CharField(max_length=50, default='Unknown')
    description = models.TextField(blank=True, null=True)
    full_name = models.CharField(max_length=100, default='John Doe')
    email = models.EmailField(default='example@example.com')
    address = models.CharField(max_length=255, default='123 Default St')
    city = models.CharField(max_length=100, default='Default City')
    state = models.CharField(max_length=100, default='Default State')
    zip_code = models.CharField(max_length=20, default='00000')
    name_on_card = models.CharField(max_length=100, default='John Doe')
    card_number = models.CharField(max_length=20, default='0000000000000000')
    exp_month = models.CharField(max_length=2, default='01')
    exp_year = models.CharField(max_length=4, default='2025')
    cvv = models.CharField(max_length=4, default='000')

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.date}"

