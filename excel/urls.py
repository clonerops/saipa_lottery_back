from django.urls import path
from .views import Export_SalePlan_Excel
from django.views.decorators.csrf import csrf_exempt

app_name = 'Excel'
urlpatterns = [
    path('export_saleplan', csrf_exempt(Export_SalePlan_Excel.as_view()), name='Export_Excel')
]
