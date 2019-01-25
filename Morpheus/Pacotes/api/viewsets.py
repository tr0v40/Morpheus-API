from rest_framework.viewsets import ModelViewSet
from Pacotes.api.serializers import PacotesSerializer
from Pacotes.models import Pacotes

class PacotesViewSet(ModelViewSet):
    queryset = Pacotes.objects.all()
    serializer_class = PacotesSerializer