from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Posts
from .forms import postForm
from django.contrib import messages
from posts.models import Author
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# Create your views here.


def postView(request, slug, pk):

    post = get_object_or_404(Posts, pk=pk)
    return render(request, 'post.html', {'post': post})


def createPost(request):
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(User, username=request.user.username)
            author = get_object_or_404(Author, user=user)
            f = form.save(commit=False)
            f.author = author
            f.save()
            messages.success(request, 'Your article is posted!.')
            return HttpResponseRedirect(reverse('landing:index'))

        else:
            return render(request, 'createpost.html', {'form': form})

    else:
        form = postForm()
        return render(request, 'createpost.html', {'form': form})
