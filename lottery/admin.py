from django.contrib import admin

# Register your models here.
from lottery.models import SalePlan, SalePlanDetail

admin.site.register(SalePlan)
admin.site.register(SalePlanDetail)


