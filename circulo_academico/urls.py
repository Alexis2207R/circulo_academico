from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Apps core
    path('', include('core.urls')),
    # App Admin
    path("admin/", admin.site.urls),
]
