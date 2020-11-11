
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    fullName = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['fullName', 'username', 'email',
                  'password1', 'password2']
