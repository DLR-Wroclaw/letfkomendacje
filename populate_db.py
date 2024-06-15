
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")

import django

django.setup()

from django.contrib.auth.models import User

from leftkomendacje.models import Bookmark, Comment

#not
User.objects.create_superuser(username='admin', email='admin@example.com', password='adminpassword')

for num in range(1,20):
    b= Bookmark(author=User.objects.get(username="admin"), title=f'title_{num}', url=f'/dupa/{num}')
    b.save()
    


