from django.urls import path
from app import views
from django.conf import settings
from django.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_3),
    path('index2/', views.index_2),
    path('__debug__/', include('debug_toolbar.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
