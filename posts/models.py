from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Posts(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    text = models.TextField(unique=True)
    overview = models.CharField(max_length=300)
    timeStamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField()
    comment = models.IntegerField(default=0)
    likes = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    def getSlug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        url = reverse('posts:postView', kwargs={
                      'pk': self.pk, 'slug': self.getSlug()})
        return url

    @property
    def getLikesCount(self):
        return self.likes.count()


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    text = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return text
