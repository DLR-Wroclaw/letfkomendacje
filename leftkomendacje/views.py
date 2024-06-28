from datetime import date, timedelta
from typing import Any

from django.views.generic import DetailView, ListView, TemplateView

from .models import Bookmark, Comment


class BestListView(ListView):
    template_name = "best_list.html"
    context_object_name = "bookmarks"

    def get_queryset(self):
        delta=self.kwargs.get('delta')
        if delta==0:
            return Bookmark.objects.order_by('-rating')
        
        if not delta:
            delta= 5
        return Bookmark.objects.filter(created_at__gte=date.today()-timedelta(days=delta),is_archived=False).order_by('-rating')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data=super().get_context_data(**kwargs)
        data['delta']=self.kwargs.get('delta')
        return data
    
class FreshListView(ListView):
    template_name = "fresh_list.html"
    context_object_name = "bookmarks"

    def get_queryset(self):
        delta=self.kwargs.get('delta')
        if delta==0:
            return Bookmark.objects.order_by('-created_at')
        
        if not delta:
            delta= 5
        return Bookmark.objects.filter(created_at__gte=date.today()-timedelta(days=delta), is_archived=False).order_by('-created_at')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data=super().get_context_data(**kwargs)
        data['delta']=self.kwargs.get('delta')
        return data

class NewListView(ListView):
    template_name = "new_list.html"
    context_object_name = "bookmarks"

    def get_queryset(self):
        return Bookmark.objects.all().order_by('created_at')[0:10]


class BookmarkView(TemplateView):
    template_name = "bookmark.html"
    context_object_name = "bookmark"
    model= Bookmark

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        def get_replies_for_comment(comment: Comment):
            replies= Comment.objects.filter(parent_comment=comment)
            if not replies:
                return {'parent':comment,'children':[]}
            else:
                return {'parent':comment, 'children':[get_replies_for_comment(reply) for reply in replies]}

        data=super().get_context_data(**kwargs)
        data['bookmark']= Bookmark.objects.filter(id=kwargs['id'])[0]
        comments= Comment.objects.filter(parent_bookmark=data['bookmark'], parent_comment=None).order_by('created_at')
        data['comments'] = [get_replies_for_comment(comment) for comment in comments]
        
        return data