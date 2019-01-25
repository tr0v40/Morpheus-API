from rest_framework.viewsets import ModelViewSet
from Clientes.models import Clientes
from .serializers import ClienteSerializer

class ClientesViewSet(ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer