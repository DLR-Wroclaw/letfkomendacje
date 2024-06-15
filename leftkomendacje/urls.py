from django.urls import include, path

from leftkomendacje.views import BestListView

urlpatterns = [
    path("", BestListView.as_view(), name="best_list"),

]