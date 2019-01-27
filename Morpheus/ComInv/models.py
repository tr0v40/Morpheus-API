from django.db import models
from django.db.models.fields import IntegerField
from Clientes.models import Clientes
from Fornecedores.models import Fornecedores
from Materiais.models import Materiais
from Pacotes.models import Pacotes
from Portos.models import Portos


class CommercialInvoice(models.Model):
    CI_ident = models.CharField(max_length=20, default="nada")
    data = models.IntegerField()
    peso_bruto_total = models.DecimalField(max_digits=10, decimal_places=3)
    peso_liq_total = models.DecimalField(max_digits=10, decimal_places=3)
    booking = models.CharField(max_length=50)
    usa_total = models.DecimalField(max_digits=10, decimal_places=2)
    soma_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_embarque = models.IntegerField()
    obs = models.TextField()
    ci_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True, blank=True)
    ci_fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE, null=True, blank=True)
    ci_porto = models.ManyToManyField(Portos,  blank=True)
    

    def __str__(self):
        return self.CI_ident
