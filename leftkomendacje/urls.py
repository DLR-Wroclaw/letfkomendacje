from django.urls import include, path

from leftkomendacje.views import BestListView, BookmarkView

urlpatterns = [
    path("", BestListView.as_view(), name="best_list"),
    path("bookmark/<int:id>/", BookmarkView.as_view(), name='bookmark')

]