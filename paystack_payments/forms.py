from .models import CustomerInfo
from django import forms


class CustomerInfo(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = '__all__'