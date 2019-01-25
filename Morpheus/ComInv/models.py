from django.db import models
from django.db.models.fields import IntegerField
from pytz import timezone


class CommercialInvoice(models.Model):
    CI_ident = models.CharField(max_length=20, default="nada")
    data = models.IntegerField()
    qtde = models.IntegerField()
    peso_unit = models.DecimalField(max_digits=10, decimal_places=3)
    peso_liq = models.DecimalField(max_digits=10, decimal_places=3)
    peso_bruto_total = models.DecimalField(max_digits=10, decimal_places=3)
    peso_liq_total = models.DecimalField(max_digits=10, decimal_places=3)
    booking = models.CharField(max_length=50)
    valor_usa = models.DecimalField(max_digits=10, decimal_places=2)
    usa_total = models.DecimalField(max_digits=10, decimal_places=2)
    soma_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_embarque = models.IntegerField()
    obs = models.TextField()

    def __str__(self):
        return self.CI_ident
