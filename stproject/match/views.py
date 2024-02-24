# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TeamA_Q1
from .serializers import TeamA_Q1Serializer

class TeamA_Q1CreateUpadateView(APIView):
    def post(self, request, format=None):
        time = request.data.get('time')

        existing_entry = TeamA_Q1.objects.filter(time=time).first()

        
        if existing_entry:
            existing_entry.delete()

        serializer = TeamA_Q1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TeamA_Q1FetchView(APIView):
    def get(self, request, format=None):
        queryset = TeamA_Q1.objects.all()  
        serializer = TeamA_Q1Serializer(queryset, many=True)
        return Response(serializer.data)