from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Posts(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    overview = models.CharField(max_length=300)
    timeStamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField()
    comment = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    text = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return text
