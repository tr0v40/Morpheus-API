from rest_framework.serializers import ModelSerializer
from Clientes.models import Clientes

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Clientes
        fields = (
            'id', 'cliente', 'rua', 'num', 'bairro', 'cidade', 
            'estado', 'pais', 'cep', 'cnpj', 'tel', 
            'fax', 'cel', 'contato' )