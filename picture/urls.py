from django.contrib import admin
from django.urls import path

from.views import home_views
urlpatterns = [
    path('home/', home_views,name='home')
]