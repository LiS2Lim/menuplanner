from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('photo-add/', admin.site.urls),
    path('common/', include('common.urls')),
    path('', include('cook.urls')),
]
