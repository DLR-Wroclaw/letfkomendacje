from django.urls import include, path
from django.views.generic.base import RedirectView

from leftkomendacje.views import BestListView, BookmarkView, FreshListView

urlpatterns = [
    path("", RedirectView.as_view(url="best/5")),
    path("fresh/<int:delta>", FreshListView.as_view(), name="fresh_list"),
    path("best/<int:delta>", BestListView.as_view(), name="best_list"),
    path("bookmark/<int:id>/", BookmarkView.as_view(), name='bookmark')

]