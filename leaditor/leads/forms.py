from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'industry', 'website_visits', 'email_open_rate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lead Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lead Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'industry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Industry'}),
            'website_visits': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Website Visits'}),
            'email_open_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Email Open Rate (%)'}),
        }
