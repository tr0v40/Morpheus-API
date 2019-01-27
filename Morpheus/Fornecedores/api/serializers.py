from rest_framework.serializers import ModelSerializer
from Fornecedores.models import Fornecedores

class FornecedoresSerializer(ModelSerializer):
    class Meta:
        model = Fornecedores
        fields = (
            'id', 'empresa', 'rua', 'num', 'bairro', 'cidade', 
            'estado', 'pais', 'cep', 'cnpj', 
            'tel', 'fax', 'cel', 'logo'
            )