from django.urls import path
from .views import RetrieveAllSalePlans, RetrieveDetailSalePlans

app_name = 'lottery'
urlpatterns = [
    path('saleplans', RetrieveAllSalePlans.as_view(),  name='retrieve_all_saleplans'),
    path('saleplans/<int:pk>',  RetrieveDetailSalePlans.as_view(),  name='retrieve_saleplans_details')
]