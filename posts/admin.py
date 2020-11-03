from django.contrib import admin
from .models import Author, Posts, Comments


# Register your models here.

admin.site.site_header = "Blog Admin"
admin.site.site_title = "Blog admin area"
admin.site.index_title = "welcome to the Blog admin area"


class CommentsInline(admin.TabularInline):
    model = Comments


class PostsAdmin(admin.ModelAdmin):
    inlines = [CommentsInline]


admin.site.register(Author)
admin.site.register(Posts, PostsAdmin)
