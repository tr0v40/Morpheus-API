from rest_framework.viewsets import ModelViewSet
from .serializers import FornecedoresSerializer
from Fornecedores.models import Fornecedores


class FornecedoresViewSet(ModelViewSet):

    queryset = Fornecedores.objects.all()
    serializer_class = FornecedoresSerializer