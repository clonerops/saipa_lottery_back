import datetime
from django_jalali.db import models as jmodels
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone


class SalePlan(models.Model):
    objects = jmodels.jManager()
    Id = models.AutoField(primary_key=True)
    RegisterStartDate = jmodels.jDateTimeField(verbose_name='تاریخ شروع ثبت نام')
    RegisterEndDate = jmodels.jDateTimeField(verbose_name='تاریخ پایان ثبت نام')
    LotteryDate = jmodels.jDateTimeField(verbose_name='تاریخ قرعه کشی')
    Description = models.CharField(max_length=255, verbose_name='توضیحات')
    ExtraDescription = models.TextField(verbose_name='توضیحات اضافی')
    LastModifyBy = models.CharField(max_length=255, verbose_name='اخرین تغییر توسط')
    LastModified = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')
    CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ایجاد شده توسط')
    CreatedAt = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

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


class Applicants(models.Model):
    Id = models.AutoField(primary_key=True)
    Srl = models.IntegerField()
    LotterySrl = models.IntegerField()
    SalePlan = models.ForeignKey(SalePlan, on_delete=models.CASCADE, related_name='SalePlan')
    NationalCode = models.CharField(max_length=11)
    FirstName = models.CharField(max_length=255, null=True, blank=True)
    LastName = models.CharField(max_length=255, null=True, blank=True)
    Gender = models.IntegerField(null=True, blank=True)
    MobileNo = models.CharField(max_length=11, null=True, blank=True)
    Sheba = models.CharField(max_length=255, null=True, blank=True)
    CompanyId = models.IntegerField()
    SaleTypeId = models.IntegerField()
    Javani = models.IntegerField()
    CarRow = models.IntegerField()
    CarName = models.CharField(max_length=255, null=True, blank=True)
    ProvinceId = models.IntegerField()
    Province = models.CharField(max_length=255, null=True, blank=True)
    CityId = models.IntegerField()
    City = models.CharField(max_length=255, null=True, blank=True)
    CrclRow = models.IntegerField()
    AnnounceRow = models.CharField(max_length=255)
    IsValid = models.BooleanField()
    LotteryDescription = models.CharField(max_length=255, null=True, blank=True)
    Company = models.CharField(max_length=255, null=True, blank=True)
    AnnounceType = models.CharField(max_length=255, null=True, blank=True)
    PlaqueValidation = models.IntegerField()
    CertificateValidaion = models.IntegerField()
    SamavaValidation = models.IntegerField()
    LotterySalePlanId = models.IntegerField()
    Created = models.DateTimeField(auto_now_add=True)
    Modified = models.DateTimeField(auto_now=True)


class ValidApplicants(models.Model):
    Id = models.AutoField(primary_key=True)
    Srl = models.IntegerField()
    LotterySrl = models.IntegerField()
    SalePlan = models.ForeignKey(SalePlan, on_delete=models.CASCADE, related_name='ValidSalePlan')
    NationalCode = models.CharField(max_length=11)
    FirstName = models.CharField(max_length=255, null=True, blank=True)
    LastName = models.CharField(max_length=255, null=True, blank=True)
    Gender = models.IntegerField(null=True, blank=True)
    MobileNo = models.CharField(max_length=11, null=True, blank=True)
    Sheba = models.CharField(max_length=255, null=True, blank=True)
    CompanyId = models.IntegerField()
    SaleTypeId = models.IntegerField()
    Javani = models.IntegerField()
    CarRow = models.IntegerField()
    CarName = models.CharField(max_length=255, null=True, blank=True)
    ProvinceId = models.IntegerField()
    Province = models.CharField(max_length=255, null=True, blank=True)
    CityId = models.IntegerField()
    City = models.CharField(max_length=255, null=True, blank=True)
    CrclRow = models.IntegerField()
    AnnounceRow = models.CharField(max_length=255)
    IsValid = models.BooleanField()
    LotteryDescription = models.CharField(max_length=255, null=True, blank=True)
    Company = models.CharField(max_length=255, null=True, blank=True)
    AnnounceType = models.CharField(max_length=255, null=True, blank=True)
    PlaqueValidation = models.IntegerField()
    CertificateValidaion = models.IntegerField()
    SamavaValidation = models.IntegerField()
    LotterySalePlanId = models.IntegerField()
    Created = models.DateTimeField(auto_now_add=True)
    Modified = models.DateTimeField(auto_now=True)


class Winner(models.Model):
    Id = models.AutoField(primary_key=True)
    Srl = models.IntegerField()
    LotterySrl = models.IntegerField()
    SalePlan = models.ForeignKey(SalePlan, on_delete=models.CASCADE, related_name='WinnerSalePlan')
    NationalCode = models.CharField(max_length=11)
    FirstName = models.CharField(max_length=255, null=True, blank=True)
    LastName = models.CharField(max_length=255, null=True, blank=True)
    Gender = models.IntegerField(null=True, blank=True)
    MobileNo = models.CharField(max_length=11, null=True, blank=True)
    Sheba = models.CharField(max_length=255, null=True, blank=True)
    CompanyId = models.IntegerField()
    SaleTypeId = models.IntegerField()
    Javani = models.IntegerField()
    CarRow = models.IntegerField()
    CarName = models.CharField(max_length=255, null=True, blank=True)
    ProvinceId = models.IntegerField()
    Province = models.CharField(max_length=255, null=True, blank=True)
    CityId = models.IntegerField()
    City = models.CharField(max_length=255, null=True, blank=True)
    CrclRow = models.IntegerField()
    AnnounceRow = models.CharField(max_length=255)
    IsValid = models.BooleanField()
    LotteryDescription = models.CharField(max_length=255, null=True, blank=True)
    Company = models.CharField(max_length=255, null=True, blank=True)
    AnnounceType = models.CharField(max_length=255, null=True, blank=True)
    PlaqueValidation = models.IntegerField()
    CertificateValidaion = models.IntegerField()
    SamavaValidation = models.IntegerField()
    LotterySalePlanId = models.IntegerField()
    Created = models.DateTimeField(auto_now_add=True)
    Modified = models.DateTimeField(auto_now=True)
