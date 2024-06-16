from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


class Bookmark(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    url = models.URLField()
    rating= models.PositiveIntegerField(default=0)
    is_duplicate=models.BooleanField(default=False)
    is_archived=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}: {self.title}-{self.url}'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    content= models.CharField(max_length=200)
    parent_bookmark= models.ForeignKey(Bookmark, on_delete=models.CASCADE)
    parent_comment= models.ForeignKey('self', blank=True,null=True, on_delete=models.CASCADE) # If not none- comment is a reply

    def clean(self):
        if self.parent_comment.id == self.id:
            raise ValidationError("Parent comment can't be self")
        
