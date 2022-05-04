from django.contrib import admin

from works_core.models import *

# Регистрация модели City
admin.site.register(City)

# Регистрация модели Specialization
admin.site.register(Specialization)

# Регистрация модели Vacancy
admin.site.register(Vacancy)
