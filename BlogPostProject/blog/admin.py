from django.contrib import admin
from .models import Author, Blog, Like, Comment

# Register your models here.


@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'create_time')


@admin.register(Like)
class Like(admin.ModelAdmin):
    list_display = ('liker', 'blog')


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ('commenter', 'blog')
