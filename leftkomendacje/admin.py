from django.contrib import admin

from .models import Bookmark, Comment

# Register your models here.

admin.site.register([Bookmark,Comment])
