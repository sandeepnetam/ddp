
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="index"),
    path('ddp/', Ddp.as_view(), name="ddp"),
]