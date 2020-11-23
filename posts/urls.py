from django.urls import path, include
from . import views
app_name = 'posts'

urlpatterns = [
    path('<int:pk>-<slug:slug>', views.postView, name='postView'),
    path('create/', views.createPost, name='createPost'),
    path('', views.likePosts, name='likeView'),
]
