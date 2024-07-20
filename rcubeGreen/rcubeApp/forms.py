from django import forms
from .models import PaymentMethod

class PaymentMethodForm(forms.ModelForm):
    total_amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.HiddenInput())  # Added
    class Meta:
        model = PaymentMethod
        fields = ['full_name', 'email', 'address', 'city', 'state', 'zip_code', 'name_on_card', 'card_number', 'exp_month', 'exp_year', 'cvv', 'total_amount'] # Modified