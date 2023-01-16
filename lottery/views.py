from django.shortcuts import render
from rest_framework import generics
from .models import Lottery, SalePlan
from .serializers import LotterySerializers, SalePlanSerializers


# Create your views here.
class RetrieveAllSalePlans(generics.ListAPIView):
    queryset = SalePlan.objects.all()
    serializer_class = SalePlanSerializers


class RetrieveAllLottories(generics.ListAPIView):
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializers
