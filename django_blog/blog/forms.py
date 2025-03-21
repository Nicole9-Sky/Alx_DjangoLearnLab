from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['content']
        
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) < 2:
            raise forms.ValidationError("Comment is too short!")
        return content    