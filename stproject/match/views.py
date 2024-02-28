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
        shot_type = request.query_params.get('shot_type')
        
        # Check if shot_type is None or empty string
        if shot_type is None or shot_type.strip() == '':
            queryset = TeamA.objects.all()  # Fetch all objects
        else:
            # Validate the shot type
            if shot_type not in ['2P', '3P','FREE THROW','FOUL','TEAM REBOUND' , 'INBOUND','TURNOVER', 'SUBSTITUTION']:
                return Response({'message': 'Invalid shot type'}, status=status.HTTP_400_BAD_REQUEST)
            
            queryset = TeamA.objects.filter(shot=shot_type)
        
        serializer = TeamASerializer(queryset, many=True)
        return Response(serializer.data)

# TeamA fetch time on basis of shot 
class TeamATimeListView(APIView):
    def get(self, request, format=None):
        shot_type = request.query_params.get('shot_type')
        
        # Check if shot_type is None or empty string
        if shot_type is None or shot_type.strip() == '':
            queryset = TeamA.objects.all()  # Fetch all objects
        else:
            # Validate the shot type
            if shot_type not in ['2P', '3P','FREE THROW','FOUL','TEAM REBOUND' , 'INBOUND','TURNOVER', 'SUBSTITUTION']:
                return Response({'message': 'Invalid shot type'}, status=status.HTTP_400_BAD_REQUEST)
            
            queryset = TeamA.objects.filter(shot=shot_type)
        
        # Get times and corresponding shot type
        times_and_shot = queryset.exclude(time__isnull=True).values_list('shot', 'time')
        
        # Convert queryset to list of dictionaries
        response_data = [{'shot': shot, 'time': time} for shot, time in times_and_shot]
        
        return Response(response_data)
    
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
        shot_type = request.query_params.get('shot_type')
        
        # Check if shot_type is None or empty string
        if shot_type is None or shot_type.strip() == '':
            queryset = TeamB.objects.all()  # Fetch all objects
        else:
            # Validate the shot type
            if shot_type not in ['2P', '3P','FREE THROW','FOUL','TEAM REBOUND' , 'INBOUND','TURNOVER', 'SUBSTITUTION']:
                return Response({'message': 'Invalid shot type'}, status=status.HTTP_400_BAD_REQUEST)
            
            queryset = TeamB.objects.filter(shot=shot_type)
        
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

# TeamB fetch time fetch time on basis of shot 
class TeamBTimeListView(APIView):
    def get(self, request, format=None):
        shot_type = request.query_params.get('shot_type')
        
        # Check if shot_type is None or empty string
        if shot_type is None or shot_type.strip() == '':
            queryset = TeamB.objects.all()  # Fetch all objects
        else:
            # Validate the shot type
            if shot_type not in ['2P', '3P','FREE THROW','FOUL','TEAM REBOUND' , 'INBOUND','TURNOVER', 'SUBSTITUTION']:
                return Response({'message': 'Invalid shot type'}, status=status.HTTP_400_BAD_REQUEST)
            
            queryset = TeamB.objects.filter(shot=shot_type)
        
        # Get times and corresponding shot type
        times_and_shot = queryset.exclude(time__isnull=True).values_list('shot', 'time')
        
        # Convert queryset to list of dictionaries
        response_data = [{'shot': shot, 'time': time} for shot, time in times_and_shot]
        
        return Response(response_data)