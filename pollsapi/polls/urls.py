from django.urls import path
from .apiviews import PollDetail, PollList
from .views import poll_list, polls_detail


urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail")
]
