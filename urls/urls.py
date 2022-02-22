from xml.etree.ElementInclude import include

from django.conf import settings

from django.contrib import admin
from django.urls import path

from django.urls import path, include


urlpatterns = [
    path(settings.ADMIN_SITE_URL, admin.site.urls),
    path('', include('app.urls')),
]

