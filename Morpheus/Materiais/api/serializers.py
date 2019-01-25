from rest_framework.serializers import ModelSerializer
from Materiais.models import Materiais

class MateriaisSerializer(ModelSerializer):
    class Meta:
        model = Materiais
        fields = ('NCM', 'material')