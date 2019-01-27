from rest_framework.serializers import ModelSerializer
from Portos.models import Portos

class PortosSerializer(ModelSerializer):
    class Meta:
        model = Portos
        fields = ('id', 'porto', 'cidade', 'pais', )