from django.urls import path

from works_accounts.views import *

# Пути приложения
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
