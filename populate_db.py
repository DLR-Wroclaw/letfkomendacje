
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")

import django

django.setup()

from django.contrib.auth.models import User

from leftkomendacje.models import Bookmark, Category, Comment

#not
User.objects.create_superuser(username='admin', email='admin@example.com', password='admin')

for num in range(1,5):
    c = Category(name= f'Category {num}', description=f'description {num}')
    c.save()

for num in range(1,20):
    b= Bookmark(author=User.objects.get(username="admin"), category= Category.objects.get(id=1) ,title=f'title_{num}', url=f'/dupa/{num}')
    b.save()
    
b= Bookmark.objects.get(id=1)
for num in range(1,10):
    com= Comment(author=User.objects.get(username="admin"), content=f'comment {num}', parent_bookmark=b)
    com.save()

