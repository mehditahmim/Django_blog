from django import forms
from posts.models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


class postForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=150, required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)
    overview = forms.CharField(max_length=300, required=True)
    thumbnail = forms.ImageField(required=False)

    class Meta:
        model = Posts
        fields = ['title', 'text', 'overview',
                  'thumbnail']
