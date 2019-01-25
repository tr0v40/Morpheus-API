from rest_framework.viewsets import ModelViewSet
from Ticket.api.serializers import TicketSerializer
from Ticket.models import Ticket

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer