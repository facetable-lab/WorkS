from django.apps import AppConfig


# Класс с настройками приложения
class WorksCoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'works_core'
    verbose_name = 'Ядро сайта (приложение по сбору вакансий)'
