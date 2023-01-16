from .models import Lottery, SalePlan
from rest_framework import serializers


class LotterySerializers(serializers.ModelSerializer):
    class Meta:
        model = Lottery
        fields = '__all__'


class SalePlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = SalePlan
        fields = '__all__'
