from rest_framework.serializers import ModelSerializer
from Pacotes.models import Pacotes


class PacotesSerializer(ModelSerializer):
    class Meta:
        model = Pacotes
        fields = ('id', 'pacote')