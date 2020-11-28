from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from .models import Posts, Comments
from .forms import postForm
from django.contrib import messages
from posts.models import Author
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import F
import json
from django.views.decorators.csrf import csrf_protect
from django.template.loader import render_to_string
# Create your views here.


def postView(request, slug, pk):
    post = get_object_or_404(Posts, pk=pk)
    comments = post.comments
    return render(request, 'post.html', {'post': post, 'comments': comments})


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


@csrf_protect
def likePosts(request):

    if request.method == "POST":

        if request.POST.get("operation") == "like_submit" and request.is_ajax():
            post_id = request.POST.get("content_id", None)
            post = get_object_or_404(Posts, pk=post_id)

            if post.likes.filter(id=request.user.id):  # already liked the content
                post.likes.remove(request.user)  # remove user from likes
                liked = False
            else:
                post.likes.add(request.user)
                liked = True
            like_count = post.getLikesCount

            ctx = {"likes_count": like_count,
                   "liked": liked, "post_id": post_id,
                   "like_count": like_count}
            return HttpResponse(json.dumps(ctx), content_type='application/json')


@csrf_protect
def comments(request):
    if request.method == "POST":
        if request.POST.get("operation") == "comment_submit" and request.is_ajax():
            post_num = request.POST.get("content_id", None)
            post = get_object_or_404(Posts, pk=post_num)
            comment = Comments()
            comment.user = request.user
            comment.post = post
            comment_text = request.POST.get("cmnt_text", None)
            comment.text = comment_text
            comment.save()
            #html = render_to_string('post.html', {'objects': objects_list})
            ctx = {'comment_text': comment_text}
            return HttpResponse(json.dumps(ctx), content_type='application/json')
