

from django.conf import settings

from django.contrib import admin
from django.urls import path

from django.urls import path 
from django.urls import include
from django.conf.urls.static import static


urlpatterns = [
    path(settings.ADMIN_SITE_URL, admin.site.urls),
    path('', include("app.urls"))
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)




