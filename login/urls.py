from django.contrib import admin
from django.urls import include, path

from.views import login_view,signup_view
urlpatterns = [
    path('', login_view, name=('login')),
    path('', signup_view, name=('signup'))
]