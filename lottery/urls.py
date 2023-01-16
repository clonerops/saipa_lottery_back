from django.urls import path
from .views import RetrieveAllSalePlans ,RetrieveAllLottories

app_name = 'lottery'
urlpatterns = [
    path('saleplans', RetrieveAllSalePlans.as_view(),  name='retrieve_all_saleplans'),
    path('lottery', RetrieveAllLottories.as_view(),  name='retrieve_all_lottery')
]