import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone


class SalePlan(models.Model):
    Id = models.AutoField(primary_key=True)
    RegisterStartDate = models.DateTimeField()
    RegisterEndDate = models.DateTimeField()
    LotteryDate = models.DateTimeField()
    Description = models.CharField(max_length=255)
    ExtraDescription = models.TextField()
    LastModifyBy = models.CharField(max_length=255)
    LastModified = models.DateTimeField(auto_now=True)
    CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Description


class SalePlanDetail(models.Model):
    Id = models.AutoField(primary_key=True)
    AnnounceNo = models.IntegerField()
    AnnounceRowNo = models.IntegerField()
    CirculationNo = models.IntegerField()
    CarRow = models.IntegerField()
    MainCapacity = models.IntegerField()
    ReserveCapacity = models.IntegerField()
    WindDistance = models.IntegerField()
    LotteryBaseNo = models.IntegerField()
    SalePlans = models.ForeignKey(SalePlan, on_delete=models.CASCADE, related_name='SalePlans')
    Description = models.TextField()
    CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    Created = models.DateTimeField(auto_now_add=True)
    LastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'اطلاعیه شماره {self.AnnounceNo} و ردیف اطلاعیه {self.AnnounceRowNo}'
