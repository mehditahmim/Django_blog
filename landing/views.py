
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from posts.models import Author, Posts, Comments
from django.urls import reverse
# Create your views here.


def index(request):
    posts = Posts.objects.all()[:4]
    return render(request, 'index.html', {'posts': posts})
