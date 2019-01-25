from rest_framework.viewsets import ModelViewSet
from Materiais.models import Materiais
from .serializers import MateriaisSerializer

class MateriaisViewSet(ModelViewSet):

    queryset = Materiais.objects.all()
    serializer_class = MateriaisSerializer