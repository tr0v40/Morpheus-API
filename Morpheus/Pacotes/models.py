from django.db import models

class Pacotes(models.Model):
    pacote = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.pacote