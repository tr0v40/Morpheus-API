from rest_framework.serializers import ModelSerializer
from ComInv.models import CommercialInvoice

class CommercialInvoiceSerializer(ModelSerializer):
    class Meta:
        model = CommercialInvoice
        fields = (
            'CI_ident', 'data', 'qtde', 'peso_unit', 
            'peso_liq', 'peso_bruto_total', 'peso_liq_total', 
            'booking', 'valor_usa', 'usa_total', 'soma_total', 
            'data_embarque', 'obs'
        )