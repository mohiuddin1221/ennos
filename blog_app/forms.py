from django import forms
from .models import contact

class contactform(forms.ModelForm):
    class Meta:
        model = contact  # Use = instead of :
        fields = ['name', 'email', 'subject', 'message']

