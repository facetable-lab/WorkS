from django.contrib import admin
from django.urls import path

from works_core.views import home_view

# Пути приложения
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
]
