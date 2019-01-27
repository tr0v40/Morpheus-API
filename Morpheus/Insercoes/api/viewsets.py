from rest_framework.viewsets import ModelViewSet
from .serializers import InsercaoSerializer
from Insercoes.models import Insercao

class InsercaoViewSet(ModelViewSet):
    queryset = Insercao.objects.all()
    serializer_class = InsercaoSerializer