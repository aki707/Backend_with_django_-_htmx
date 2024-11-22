from django.forms import ModelForm
from django import forms
from .models import *


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url','body', 'tags']
        labels = {
            'body': 'Caption',
            'tags': 'Category'
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3,'placeholder': 'Add a Caption...' ,'class': 'font1 text-4xl'}),
            'url': forms.TextInput(attrs={'placeholder': 'Add a URL...'}),
            'tags': forms.CheckboxSelectMultiple(),
        }
        
class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            'body': '',
            'tags': 'Category'
            
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3,'class': 'font1 text-4xl'}),
            'tags': forms.CheckboxSelectMultiple(),
            # 'url': forms.TextInput(attrs={'placeholder': 'Add a URL...'}),
            # 'title': forms.TextInput(attrs={'placeholder': 'Add a Title...'}),
            # 'artist': forms.TextInput(attrs={'placeholder': 'Add an Artist...'}),
        }