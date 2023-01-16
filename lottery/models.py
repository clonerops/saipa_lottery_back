import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.utils import timezone


class Lottery(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True)
    Title = models.CharField(max_length=255)
    AnnounceNo = models.BigIntegerField()
    CarRow = models.IntegerField()

    def __str__(self):
        return self.Title


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
