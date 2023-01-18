from django.contrib import admin
from lottery.models import SalePlan
from import_export import resources


class SalePlanResource(resources.ModelResource):
    def get_export_headers(self):
        headers = super().get_export_headers()
        print(headers)
        for i, h in enumerate(headers):
            if h == 'RegisterStartDate':
                headers[i] = "تاریخ شروع ثبت نام"
            if h == 'Description':
                headers[i] = "توضیحات"
        return headers

    class Meta:
        model = SalePlan
        fields = ('RegisterStartDate', 'Description')
        export_order = ('RegisterStartDate', 'Description')

    def dehydrate_RegisterStartDate(self, obj):
        return obj.RegisterStartDate.strftime("%Y-%m-%d")
