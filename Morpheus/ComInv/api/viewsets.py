from rest_framework.viewsets import ModelViewSet
from ComInv.api.serializers import CommercialInvoiceSerializer
from ComInv.models import CommercialInvoice


class CommercialInvoiceViewSet(ModelViewSet):
    queryset = CommercialInvoice.objects.all()
    serializer_class = CommercialInvoiceSerializer