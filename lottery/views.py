from django.shortcuts import render
from rest_framework import generics
from .models import Lottery
from .serializers import LotterySerializers


# Create your views here.

class RetrieveAllLottories(generics.ListAPIView):
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializers
