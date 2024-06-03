from django.urls import path
from .views import *

urlpatterns = [
    path('create_match/', CreateMatch.as_view(), name='create_match'),
    path('delete_match/', DeleteMatch.as_view(), name='delete_match'),
    path('update_match/', UpdateMatch.as_view(), name='update_match'),
    path('Retrieve_match/', RetrieveMatch.as_view(), name='Retrieve_match'),
    # Other URL patterns...
]
