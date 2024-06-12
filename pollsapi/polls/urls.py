from django.urls import path
from .apiviews import PollDetail, PollList, ChoiceList, CreateVote
from .views import poll_list, polls_detail

urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="vote_list"),
]
