from django.db import models
from jsonfield import JSONField

from works_core.utils import from_cyrillic_to_slug


def default_urls():
    return {'hh_ru': '',
            'rabota_ru': '',
            'habr_career': ''}


# Модель Города
class City(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название населенного пункта', unique=True)
    slug = models.CharField(max_length=40, blank=True, unique=True)

    # Русификация
    class Meta:
        verbose_name = 'Название населенного пункта'
        verbose_name_plural = 'Название населенных пунктов'

    # Отображение по названию города
    def __str__(self):
        return self.name

    # Переопределенный метод, при созранении объекта автоматически генерирует slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_slug(str(self.name))
        super().save(*args, **kwargs)


# Модель Специализации (Языка программирования)
class Specialization(models.Model):
    name = models.CharField(max_length=25, verbose_name='Язык программирования', unique=True)
    slug = models.CharField(max_length=40, blank=True, unique=True)

    # Русификация
    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    # Отображение по названию города
    def __str__(self):
        return self.name

    # Переопределенный метод, при созранении объекта автоматически генерирует slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_slug(str(self.name))
        super().save(*args, **kwargs)


# Модель для Вакансии
class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Название вакансии')
    company = models.CharField(max_length=250, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание вакансии')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')  # поле со связкой к модели города
    specialization = models.ForeignKey('Specialization', on_delete=models.CASCADE,
                                       verbose_name='Язык программирования')  # поле со связкой к модели специализации
    time_stamp = models.DateField(auto_now_add=True)

    # Русификация
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-time_stamp']

    # Отображение по названию города
    def __str__(self):
        return self.title


# Модель для ошибок
class Error(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    data = JSONField(null=True)


# Модель для URL парсера
class Url(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    specialization = models.ForeignKey('Specialization', on_delete=models.CASCADE,
                                       verbose_name='Язык программирования')
    url_data = JSONField(null=True, default=default_urls)

    class Meta:
        unique_together = ('city', 'specialization')
