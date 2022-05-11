from django.contrib import admin

from works_core.models import *


# Кастомизация отображения в админке
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


# Кастомизация отображения в админке
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


# Кастомизация отображения в админке
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'specialization', 'company')
    list_display_links = ('company', 'city', 'specialization')


# Регистрация модели City
admin.site.register(City, CityAdmin)

# Регистрация модели Specialization
admin.site.register(Specialization, SpecializationAdmin)

# Регистрация модели Vacancy
admin.site.register(Vacancy, VacancyAdmin)
