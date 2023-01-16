from django.contrib import admin

# Register your models here.
from lottery.models import Lottery, SalePlan

admin.site.register(Lottery)
admin.site.register(SalePlan)

