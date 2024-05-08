from django.contrib import admin
from django.urls import include, path

from login import urls as login_app_urls
from picture import urls as picture_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(login_app_urls)),
    path('picture/', include(picture_app_urls)),
]
