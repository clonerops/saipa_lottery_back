from django.urls import path
from .views import RetrieveAllLottories

app_name = 'lottery'
urlpatterns = [
    path('lottery', RetrieveAllLottories.as_view(),  name='retrieve_all_lottery')
]