from django.shortcuts import render, get_object_or_404
from posts.models import Author, Posts
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


def profileView(request, username):

    user = get_object_or_404(User, username=username)
    author = Author.objects.get(user=user)
    posts = Posts.objects.filter(author=author)
    count = Posts.objects.filter(author=author).count()
    context = {'user': user, 'posts': posts, 'count': count}
    return render(request, 'userprofile.html', context)

# Create your views here.
