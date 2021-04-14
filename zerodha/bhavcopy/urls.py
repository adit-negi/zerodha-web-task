from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/v1/bhavcopy/name/<str:name>', search_bhavcopy),
    path('api/v1/bhavcopy/names/all', bhavcopy_all),
    path('',home_page)
]
