from django.urls import path
from .apiviews import ChoiceList, CreateVote, PollViewSet, UserCreate
# from .views import poll_list, polls_detail
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path("polls/", PollList.as_view(), name="polls_list"),
    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    # path("choices/", ChoiceList.as_view(), name="choice_list"),
    # path("vote/", CreateVote.as_view(), name="vote_list"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users", UserCreate.as_view(), name="user_create")
]

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns += router.urls
