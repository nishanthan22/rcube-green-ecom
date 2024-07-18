# admin.py
from django.contrib import admin
from .models import PaymentMethod

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date', 'method', 'description')
    search_fields = ('user__username', 'amount', 'date', 'method', 'description')
