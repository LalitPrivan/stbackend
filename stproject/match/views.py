# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TeamA,TeamB
from .serializers import TeamASerializer,TeamBSerializer

# TeamA Insert and update 
class TeamACreateUpadateView(APIView):
    def post(self, request, format=None):
        time = request.data.get('time')

        existing_entry = TeamA.objects.filter(time=time).first()

        
        if existing_entry:
            existing_entry.delete()

        serializer = TeamASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# TeamA fetch
class TeamAFetchView(APIView):
    def get(self, request, format=None):
        queryset = TeamA.objects.exclude(
            made__isnull=True,
            made_SJN__isnull=True,
        )
        
        serializer = TeamASerializer(queryset, many=True)
        return Response(serializer.data)

# TeamA delete
class TeamADeleteView(APIView):
    def delete(self, request, format=None):
        try:
            time = request.data.get('time')
            if time is not None:
                queryset = TeamA.objects.filter(time=time)
                if queryset.exists():
                    queryset.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({"message": "No data found for the given time"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"message": "Time parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# TeamA fetch time
class TeamATimeListView(APIView):
    def get(self, request, format=None):
        times = TeamA.objects.values_list('time', flat=True)  
        return Response(times)
    
# TeamB Insert and update 
class TeamBCreateUpadateView(APIView):
    def post(self, request, format=None):
        time = request.data.get('time')

        existing_entry = TeamB.objects.filter(time=time).first()

        
        if existing_entry:
            existing_entry.delete()

        serializer = TeamBSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# TeamB fetch
class TeamBFetchView(APIView):
    def get(self, request, format=None):
        queryset = TeamB.objects.exclude(
            made__isnull=True,
            made_SJN__isnull=True,
        )
        
        serializer = TeamBSerializer(queryset, many=True)
        return Response(serializer.data)

# TeamB delete
class TeamBDeleteView(APIView):
    def delete(self, request, format=None):
        try:
            time = request.data.get('time')
            if time is not None:
                queryset = TeamB.objects.filter(time=time)
                if queryset.exists():
                    queryset.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({"message": "No data found for the given time"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"message": "Time parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# TeamB fetch time
class TeamBTimeListView(APIView):
    def get(self, request, format=None):
        times = TeamB.objects.values_list('time', flat=True)  
        return Response(times)