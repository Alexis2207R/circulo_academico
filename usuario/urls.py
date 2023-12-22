from django.urls import path
from django.contrib.auth.views import PasswordChangeView, LogoutView

urlpatterns = [
    # Otras rutas...
    # ...
    # Ruta para el cambio de contraseña
    path(
        "admin/password_change/",
        PasswordChangeView.as_view(),
        name="admin_password_change",
    ),
    # Ruta para el cierre de sesión
    path("admin/logout/", LogoutView.as_view(), name="admin_logout"),
    # Otras rutas...
    # ...
]
