from django.urls import path
from .views import Export_SalePlan_Excel

app_name = 'Excel'
urlpatterns = [
    path('export_saleplan', Export_SalePlan_Excel, name='Export_Excel')
]
