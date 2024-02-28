from django.urls import path
from .views import TeamACreateUpadateView,TeamAFetchView,TeamADeleteView,TeamATimeListView,TeamBCreateUpadateView,TeamBFetchView,TeamBDeleteView,TeamBTimeListView

urlpatterns = [
    path('TeamA/', TeamACreateUpadateView.as_view(), name='TeamA_create'),
    path('TeamA/fetch/', TeamAFetchView.as_view(), name='TeamA_fetch'),
    path('TeamA/delete/', TeamADeleteView.as_view(), name='TeamA_delete'),
    path('TeamA/fetch/times', TeamATimeListView.as_view(), name='TeamA_fetch_times'),
    path('TeamB/', TeamBCreateUpadateView.as_view(), name='TeamB_create'),
    path('TeamB/fetch/', TeamBFetchView.as_view(), name='TeamB_fetch'),
    path('TeamB/delete/', TeamBDeleteView.as_view(), name='TeamB_delete'),
    path('TeamB/fetch/times', TeamBTimeListView.as_view(), name='TeamB_fetch_times'),
]