from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Poll, Choice


# Create your views here.
def poll_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {
        "results": list(polls.values("questions", "created_by__username", "pub_date"))
    }
    return JsonResponse(data)


def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {
        "results": poll.questions,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
    }
    return JsonResponse(data)
