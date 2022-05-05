from django.contrib import admin

from works_core.models import *


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'specialization', 'company')


# Регистрация модели City
admin.site.register(City, CityAdmin)

# Регистрация модели Specialization
admin.site.register(Specialization, SpecializationAdmin)

# Регистрация модели Vacancy
admin.site.register(Vacancy, VacancyAdmin)
