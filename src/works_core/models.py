from django.db import models

from works_core.utils import from_cyrillic_to_slug


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
