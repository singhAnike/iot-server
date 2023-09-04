from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.DataAPI.as_view(), name='data_api'),
]
