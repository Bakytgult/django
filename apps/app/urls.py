from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_3),
    path('index2/', views.index_2),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

