from django import forms
from .models import CustomUser  # Import your custom user model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['date_of_birth', 'profile_photo']  # Include required fields