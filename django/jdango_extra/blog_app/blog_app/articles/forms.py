from django import forms
from .import models

class createBlog(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug']