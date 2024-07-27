from django import forms
from .models import PaymentMethod
from django.core.exceptions import ValidationError
import re
from datetime import datetime


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['full_name', 'email', 'address', 'city', 'state', 'zip_code', 'name_on_card', 'card_number',
                  'exp_month', 'exp_year', 'cvv']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Regex to match the specified email format
        if not re.match(r"^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$", email):
            raise ValidationError("Invalid email format.")
        return email

    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number')
        if not re.match(r"^\d{16}$", card_number):
            raise ValidationError("Credit card number must be 16 digits.")
        return card_number

    def clean_exp_month(self):
        exp_month = self.cleaned_data.get('exp_month')
        if not re.match(r"^(0[1-9]|1[0-2])$", exp_month):
            raise ValidationError("Invalid expiration month.")
        return exp_month

    def clean_exp_year(self):
        exp_year = self.cleaned_data.get('exp_year')
        if not re.match(r"^\d{4}$", exp_year):
            raise ValidationError("Invalid expiration year.")
        current_year = datetime.now().year
        if int(exp_year) < current_year:
            raise ValidationError("Expiration year cannot be in the past.")
        return exp_year

    def clean_cvv(self):
        cvv = self.cleaned_data.get('cvv')
        if not re.match(r"^\d{3}$", cvv):  # CVV must be exactly 3 digits
            raise ValidationError("CVV must be 3 digits.")
        return cvv

    def clean_zip_code(self):
        zip_code = self.cleaned_data.get('zip_code')
        if not re.match(r"^[a-zA-Z0-9]{6}$", zip_code):  # Zip code must be 6 alphanumeric characters
            raise ValidationError("Zip code must be 6 alphanumeric digits.")
        return zip_code
