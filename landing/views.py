
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from posts.models import Author, Posts, Comments
from django.urls import reverse
# Create your views here.


def index(request):
    posts = Posts.objects.all().order_by('-timeStamp')
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')

    try:
        paginator_query_set = paginator.page(page)

    except PageNotAnInteger:
        paginator_query_set = paginator.page(1)

    except EmptyPage:
        paginator_query_set = paginator.page(paginator.num_pages)

    num_pages = paginator.num_pages
    num_pages = [n for n in range(1, num_pages+1)]
    user = request.user
    return render(request, 'index.html', {'paginator_query_set': paginator_query_set, 'num_pages': num_pages, 'user': user})
