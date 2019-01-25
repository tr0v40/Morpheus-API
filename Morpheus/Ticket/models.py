from django.db import models

class Ticket(models.Model):
    nome_balanca = models.CharField(max_length=50)
    produto = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    motorista = models.CharField(max_length=50)
    qtde_bags = models.IntegerField()
    num_bags = models.IntegerField()
    data = models.IntegerField()
    hora = models.IntegerField()
    peso_veiculo = models.DecimalField(max_digits=10, decimal_places=3)
    peso_bruto = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.placa
    