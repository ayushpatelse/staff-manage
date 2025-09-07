from django.shortcuts import render
from .serializers import TicketmasterEventSerializer,EmbeddedDataSerializer
from .api_client import TicketmasterService
# Create your views here.
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from .utils import create_events

class TicketMasterEventView(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'event/event_list.html' 

    def get(self,request):
        service = TicketmasterService()
        data = service.get_events(request.GET)
        serializer = EmbeddedDataSerializer(data) 

        return Response({'event_list':serializer.data,'search_data':request.GET})
        
