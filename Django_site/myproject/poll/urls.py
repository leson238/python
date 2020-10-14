from django.urls import path
from . import views

app_name = "poll"
urlpatterns = [
    path("", views.IndexView.as_view(), name="poll"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/result", views.ResultView.as_view(), name="result"),
    path("<int:question_id>/vote", views.vote, name="vote")
]
