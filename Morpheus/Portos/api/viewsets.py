from rest_framework.viewsets import ModelViewSet
from .serializers import PortosSerializer
from Portos.models import Portos


class PortosViewSet(ModelViewSet):
    queryset = Portos.objects.all()
    serializer_class = PortosSerializer