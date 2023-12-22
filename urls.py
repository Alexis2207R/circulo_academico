from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import PasswordChangeView, LogoutView

urlpatterns = [
    # Apps core
    path("", include("core.urls")),
    # App Admin
    path("admin/", admin.site.urls),
    path(
        "admin/password_change/",
        PasswordChangeView.as_view(),
        name="admin_password_change",
    ),
    path("admin/logout/", LogoutView.as_view(), name="admin_logout"),
]
