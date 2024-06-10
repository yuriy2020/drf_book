from django.urls import path
from .views import poll_list, polls_detail

urlpatterns = [
    path("polls/", poll_list, name="polls_list"),
    path("polls/<int:pk>/", polls_detail, name="polls_detail")
]
