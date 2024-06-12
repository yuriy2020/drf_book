from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceList(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs['pk'])
        return queryset

class CreateVote(APIView):
    serializer_class = VoteSerializer
    def post(self, request, pk, choice_pk):
        voted_by = request.data.get('voted_by')
        data = {
            'choice': choice_pk,
            'poll': pk,
            'voted_by': voted_by
        }
        my_serializer = VoteSerializer(data=data)
        if my_serializer.is_valid():
            my_serializer.save()
            return Response(my_serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(my_serializer.errors, status.HTTP_400_BAD_REQUEST)