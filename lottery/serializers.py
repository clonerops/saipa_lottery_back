
from .models import SalePlan, SalePlanDetail, Applicants
from rest_framework import serializers


class SalePlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = SalePlan
        fields = ('Id', 'RegisterStartDate', 'RegisterEndDate', 'LotteryDate', 'Description', 'ExtraDescription',)


class SalePlansShowSerializers(serializers.ModelSerializer):
    class Meta:
        model = SalePlan
        fields = ['Id', 'Description']


class SalePlansDetailSerializers(serializers.ModelSerializer):
    SalePlans = SalePlansShowSerializers(many=False, read_only=True)

    class Meta:
        model = SalePlanDetail
        fields = ['Id', 'AnnounceNo', 'AnnounceRowNo', 'CirculationNo', 'CarRow', 'MainCapacity', 'ReserveCapacity',
                  'WindDistance', 'LotteryBaseNo', 'Description', 'SalePlans']


class ApplicantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Applicants
        fields = '__all__'
