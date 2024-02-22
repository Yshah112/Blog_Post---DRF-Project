from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Author(AbstractUser):
    """ This AbstarctUser model is useful to store all user information """

    contact = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Blog(models.Model):
    """ This Blog model is useful to store all blog data """

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Like(models.Model):
    """This like model is useful to like the particular blog"""

    liker = models.ForeignKey(Author, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.liker} likes {self.blog}'


class Comment(models.Model):
    """This Comment model is useful to comment the particular blog"""

    comment = models.TextField()
    commenter = models.ForeignKey(Author, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-create_time']

    def __str__(self):
        return f'{self.commenter} comment {self.blog}'

