from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.renderers import (
                                        HTMLFormRenderer,
                                        JSONRenderer,
                                        BrowsableAPIRenderer,
                                    )
from .. import models


class Employees(APIView):
    # authentication_classes = (TokenAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CreateAssistantSerializer
    

    def get(self, request):
        employees = models.Employee.objects.all()
        serializer = serializers.EmployeeSerializer(employees, many=True)
        a_viewset = [
            'Uses actions (GET, POST)',
        ]

        return Response({'a_viewset': a_viewset, 'response': serializer.data})


    def post(self, request):
        serializer = serializers.CreateAssistantSerializer(data=request.data)
        if serializer.is_valid():
            collective_name = serializer.data.get('collective_name')
            channel_name = serializer.data.get('channel_name')
            assistant_name = serializer.data.get('assistant_name')
            assistant_id = serializer.data.get('id')
            channel_obj     = models.Channel.objects.filter(channel_name=channel_name, collective_id__collective_name=collective_name).first()
            models.Assistant.objects.create(assistant_name=assistant_name, id=assistant_id, channel=channel_obj)
            
            a_viewset = [
                'Uses actions (GET, POST)',
            ]

            return Response({'a_viewset': a_viewset, 'response': serializer.data})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
