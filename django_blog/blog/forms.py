from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
from .models import Post, Tag
from django import forms

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
    
    
class PostForm(forms.ModelForm):
    tags = forms.CharField(max_length=200, required=False, help_text="Enter tags separated by commas")
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        
    def save(self, commit=True):
        post = super().save(commit=False)
        tag_names = self.cleaned_data['tags'].split(',')
        if commit:
            post.save()
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name.strip())
                post.tags.add(tag)
        return post