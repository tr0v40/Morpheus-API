from rest_framework.serializers import ModelSerializer
from Ticket.models import Ticket

class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id','nome_balanca', 'produto', 
        'placa', 'motorista', 'qtde_bags', 
        'num_bags', 'data', 'hora', 'peso_veiculo', 
        'peso_bruto', )