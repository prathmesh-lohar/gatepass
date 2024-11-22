from rest_framework import viewsets
from userprofiles.models import gatepass,entry
from .serializers import GatepassSerializer,EntrySerializer

class GatepassViewSet(viewsets.ModelViewSet):
    queryset = gatepass.objects.all()
    serializer_class = GatepassSerializer



class EntryViewSet(viewsets.ModelViewSet):
    queryset = entry.objects.all()
    serializer_class = EntrySerializer