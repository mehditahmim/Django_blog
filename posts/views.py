from django.shortcuts import render
from .models import Posts
# Create your views here.


def postView(request, post_id):
    post = Posts.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': post})


def test(request, id):
    return render(request, contact.html)
