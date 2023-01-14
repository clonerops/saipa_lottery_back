from .models import Lottery
from rest_framework import serializers


class LotterySerializers(serializers.ModelSerializer):
    class Meta:
        model = Lottery
        fields = '__all__'
