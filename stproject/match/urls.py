from django.urls import path
from .views import TeamA_Q1CreateUpadateView,TeamA_Q1FetchView,TeamA_Q1DeleteView

urlpatterns = [
    path('teama_q1/', TeamA_Q1CreateUpadateView.as_view(), name='teama_q1_create'),
    path('teama_q1/fetch/', TeamA_Q1FetchView.as_view(), name='teama_q1_fetch'),
    path('teama_q1/delete/', TeamA_Q1DeleteView.as_view(), name='teama_q1_delete'),
]