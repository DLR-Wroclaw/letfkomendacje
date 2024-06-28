from django.contrib import admin

from .models import Bookmark, Category, Comment

# Register your models here.

admin.site.register([Category,Bookmark,Comment])
