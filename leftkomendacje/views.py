from datetime import date, timedelta

from django.views.generic import DetailView, ListView

from .models import Bookmark


class BestListView(ListView):
    template_name = "best_list.html"
    context_object_name = "bookmarks"

    def get_queryset(self):
        return Bookmark.objects.filter(created_at__gte=date.today()-timedelta(days=5)).order_by('rating')
