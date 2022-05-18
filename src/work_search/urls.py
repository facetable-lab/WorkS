from django.contrib import admin
from django.urls import path, include

from works_core.views import *

# Пути приложения
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list', list_view, name='list'),
    path('accounts/', include(('works_accounts.urls', 'works_accounts'))),
    path('', home_view, name='home'),
]
