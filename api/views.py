from rest_framework import viewsets
from userprofiles.models import gatepass,entry,FlagElement,MatchElement
from .serializers import GatepassSerializer,EntrySerializer,FlagElementSerializer,MatchElementSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status


class GatepassViewSet(viewsets.ModelViewSet):
    queryset = gatepass.objects.all()
    serializer_class = GatepassSerializer



class EntryViewSet(viewsets.ModelViewSet):
    queryset = entry.objects.all()
    serializer_class = EntrySerializer
    
    

class FlagElementViewSet(viewsets.ViewSet):
    
    def list(self, request):
        # Fetch the only existing entry
        flag_element = FlagElement.objects.first()
        if flag_element:
            serializer = FlagElementSerializer(flag_element)
            return Response(serializer.data)
        return Response({'detail': 'No flag element found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        # Since there should be only one entry, update the existing entry or create the first one if it doesn't exist
        data = request.data
        flag = data.get('flag', None)
        if flag is not None:
            # If the entry exists, update it
            flag_element, created = FlagElement.objects.get_or_create(id=1)  # Ensure only 1 entry exists
            flag_element.flag = flag
            flag_element.save()
            serializer = FlagElementSerializer(flag_element)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'Flag value is required'}, status=status.HTTP_400_BAD_REQUEST)
    


class MatchElementViewSet(viewsets.ViewSet):

    def list(self, request):
        # Fetch the only existing entry
        match_element = MatchElement.objects.first()
        if match_element:
            serializer = MatchElementSerializer(match_element)
            return Response(serializer.data)
        return Response({'detail': 'No match element found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        # Update the existing entry or create the first one if it doesn't exist
        data = request.data
        real_t_match = data.get('real_t_match', None)

        if real_t_match is None:
            return Response({'detail': 'real_t_match value is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the existing object or create a new one with ID=1
        match_element, created = MatchElement.objects.get_or_create(id=1)
        match_element.real_t_match = real_t_match
        match_element.save()

        serializer = MatchElementSerializer(match_element)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)