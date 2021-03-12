from django import forms
from ckeditor.fields import RichTextField
from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    details = forms.CharField()
    image = forms.FileField()
