from django.db import models
from Materiais.models import Materiais
from Pacotes.models import Pacotes
from ComInv.models import CommercialInvoice

class Insercao(models.Model):
    qtde = models.IntegerField()
    peso_unit = models.DecimalField(max_digits=10, decimal_places=3)
    peso_liq = models.DecimalField(max_digits=10, decimal_places=3)
    ins_material = models.ManyToManyField(Materiais)
    ins_pacote = models.ManyToManyField(Pacotes)
    ins_ci = models.ForeignKey(CommercialInvoice, on_delete=models.CASCADE, null=True, blank=True)

    