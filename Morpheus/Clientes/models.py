from django.db import models

class Clientes(models.Model):
    cliente = models.CharField(max_length=150, blank=False, null=False)
    rua = models.CharField(max_length=150, blank=True, null=True)
    num = models.IntegerField()
    bairro = models.CharField(max_length=150, blank=True, null=True)
    cidade = models.CharField(max_length=150, blank=True, null=True)
    estado = models.CharField(max_length=150, blank=True, null=True)
    pais = models.CharField(max_length=150, blank=True, null=True)
    cep = models.IntegerField()
    cnpj = models.IntegerField()
    tel = models.IntegerField()
    fax = models.IntegerField()
    cel = models.IntegerField()
    contato = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.cliente
    
    