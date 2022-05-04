from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)
    slug = models.CharField(max_length=40, blank=True)
