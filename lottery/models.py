from django.db import models


# Create your models here.
class Lottery(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True)
    Title = models.CharField(max_length=255)
    AnnounceNo = models.BigIntegerField()
    CarRow = models.IntegerField()

    def __str__(self):
        return self.Title


class SalePlan(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True)
    Title = models.CharField(max_length=255)
    Description = models.TextField()

    def __str__(self):
        return self.Title