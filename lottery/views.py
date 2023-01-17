from http.client import HTTPException

from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import SalePlan, SalePlanDetail
from .serializers import SalePlanSerializers, SalePlansDetailSerializers


# Create your views here.
class RetrieveAllSalePlans(generics.ListAPIView):
    queryset = SalePlan.objects.all()
    serializer_class = SalePlanSerializers


class RetrieveDetailSalePlans(generics.ListAPIView):
    serializer_class = SalePlansDetailSerializers

    def get_queryset(self):
        queryset = SalePlanDetail.objects.all()
        salePlanId = self.kwargs['pk']
        if salePlanId is not None:
            queryset = queryset.filter(SalePlans=salePlanId)
        return queryset
