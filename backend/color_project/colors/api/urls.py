# colors/api/urls.py
from django.urls import path
from .views import SwatchesView

urlpatterns = [
    path('swatches/', SwatchesView.as_view(), name='swatches'),
]