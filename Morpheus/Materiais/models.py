from django.db import models

class Materiais(models.Model):
    NCM = models.IntegerField()
    material = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.material
    