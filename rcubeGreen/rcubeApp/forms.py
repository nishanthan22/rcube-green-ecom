from django import forms
from .models import PaymentMethod

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['full_name', 'email', 'address', 'city', 'state', 'zip_code', 'name_on_card', 'card_number', 'exp_month', 'exp_year', 'cvv']