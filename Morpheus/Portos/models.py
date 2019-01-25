from django.db import models


class Portos(models.Model):
    porto = models.CharField(max_length=50)
    cidade = models.CharField(max_length=150, blank=True, null=True)
    pais = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.porto
    