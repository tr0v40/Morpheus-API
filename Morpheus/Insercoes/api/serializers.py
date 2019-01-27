from rest_framework.serializers import ModelSerializer
from Insercoes.models import Insercao


class InsercaoSerializer(ModelSerializer):
    class Meta:
        model = Insercao
        fields = (
            'id', 'qtde', 'peso_unit', 
            'peso_liq', 'ins_material', 'ins_pacote' 
            )