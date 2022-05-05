from django.apps import AppConfig


# Класс с настройками приложения
class WorksAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'works_accounts'
    verbose_name = 'Пользователи'
