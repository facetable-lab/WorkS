from django.contrib import admin
from django.urls import path

from works_core.views import *

# Пути приложения
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('list', list_view, name='list'),
]
