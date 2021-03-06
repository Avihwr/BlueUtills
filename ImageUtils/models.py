from django.db import models


class Photo(models.Model):
    file = models.ImageField()
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
