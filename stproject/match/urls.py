from django.urls import path
from .views import TeamACreateUpadateView,TeamAFetchView,TeamADeleteView,TeamATimeListView

urlpatterns = [
    path('TeamA/', TeamACreateUpadateView.as_view(), name='TeamA_create'),
    path('TeamA/fetch/', TeamAFetchView.as_view(), name='TeamA_fetch'),
    path('TeamA/delete/', TeamADeleteView.as_view(), name='TeamA_delete'),
    path('TeamA/fetch/times', TeamATimeListView.as_view(), name='TeamA_fetchtimes'),
]