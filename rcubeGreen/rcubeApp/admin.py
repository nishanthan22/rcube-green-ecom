# admin.py
from django.contrib import admin
from .models import PaymentMethod, Order, OrderItem

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date', 'product_list')
    search_fields = ('user__username', 'amount', 'date')

    def product_list(self, obj):
        return ', '.join([f"{item.product.name} (Quantity: {item.quantity})" for item in obj.order.orderitem_set.all()])

    product_list.short_description = 'Product List'

    exclude = ('method', 'description')

admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
