# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TeamA,TeamB
from .serializers import TeamASerializer,TeamBSerializer

# TeamA Insert and update 
class TeamACreateUpadateView(APIView):
    def post(self, request, format=None):
        match_time = request.data.get('match_time')

        existing_entry = TeamA.objects.filter(match_time=match_time).first()

        
        if existing_entry:
            existing_entry.delete()

        serializer = TeamASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TeamA fetch data with filter
class TeamAFetchView(APIView):
    def get(self, request, format=None):
        # Get query parameters
        quarter = request.query_params.get('quarter')
        tag = request.query_params.get('tag')
        shot_type = request.query_params.get('shot_type')
        made_sjn = request.query_params.get('made_sjn')
        shot = request.query_params.get('shot')
        
        # Initialize the queryset
        queryset = TeamA.objects.all()
        
        # Apply filters based on query parameters
        if quarter:
            queryset = queryset.filter(quarter=quarter)
        if tag:
            queryset = queryset.filter(tag=tag)
        if shot_type:
            queryset = queryset.filter(shot_type=shot_type)
        if made_sjn:
            queryset = queryset.filter(made_sjn=made_sjn)
        if shot:
            queryset = queryset.filter(shot=shot)
        
        # Order queryset by match_time
        queryset = queryset.order_by('match_time')
        
        # Serialize the filtered and ordered queryset
        serializer = TeamASerializer(queryset, many=True)
        
        return Response(serializer.data)
    
# TeamA delete
class TeamADeleteView(APIView):
    def delete(self, request, format=None):
        try:
            match_time = request.data.get('match_time')
            if match_time is not None:
                queryset = TeamA.objects.filter(match_time=match_time)
                if queryset.exists():
                    queryset.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({"message": "No data found for the given time"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"message": "Time parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TeamBCreateUpadateView(APIView):
    def post(self, request, format=None):
        match_time = request.data.get('match_time')

        existing_entry = TeamB.objects.filter(match_time=match_time).first()

        
        if existing_entry:
            existing_entry.delete()

        serializer = TeamBSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TeamB fetch data with filter
class TeamBFetchView(APIView):
    def get(self, request, format=None):
        shot_type = request.query_params.get('shot_type')
        
        # Check if shot_type is None or empty string
        if shot_type is None or shot_type.strip() == '':
            queryset = TeamB.objects.all().order_by('match_time')  # Fetch all objects ordered by time
        else:
            # Validate the shot type
            if shot_type not in ['2P', '3P','FREE THROW','FOUL','TEAM REBOUND' , 'INBOUND','TURNOVER', 'SUBSTITUTION']:
                return Response({'message': 'Invalid shot type'}, status=status.HTTP_400_BAD_REQUEST)
            
            queryset = TeamB.objects.filter(shot=shot_type).order_by('match_time')
        
        serializer = TeamBSerializer(queryset, many=True)
        return Response(serializer.data)
    
# TeamB delete
class TeamBDeleteView(APIView):
    def delete(self, request, format=None):
        try:
            match_time = request.data.get('match_time')
            if match_time is not None:
                queryset = TeamB.objects.filter(match_time=match_time)
                if queryset.exists():
                    queryset.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({"message": "No data found for the given time"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"message": "Time parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# # TeamA Insert and update 
# class TeamACreateUpadateView(APIView):
#     def post(self, request, format=None):
#         time = request.data.get('time')

#         existing_entry = TeamA.objects.filter(time=time).first()

        
#         if existing_entry:
#             existing_entry.delete()

#         serializer = TeamASerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# # TeamA fetch data on the basis of shot 
# class TeamAFetchView(APIView):
#     def get(self, request, format=None):
#         shot_type = request.query_params.get('shot_type')
        
#         # Check if shot_type is None or empty string
#         if shot_type is None or shot_type.strip() == '':
#             queryset = TeamA.objects.all().order_by('time')  # Fetch all objects ordered by time
#         else:
#             # Validate the shot type
#             if shot_type not in ['2P', '3P','FREE THROW','FOUL','TEAM REBOUND' , 'INBOUND','TURNOVER', 'SUBSTITUTION']:
#                 return Response({'message': 'Invalid shot type'}, status=status.HTTP_400_BAD_REQUEST)
            
#             queryset = TeamA.objects.filter(shot=shot_type).order_by('time')
        
#         serializer = TeamASerializer(queryset, many=True)
#         return Response(serializer.data)

# # TeamA fetch time on the basis of shot 
# class TeamATimeListView(APIView):
#     def get(self, request, format=None):
#         shot_type = request.query_params.get('shot_type')
        
#         # Check if shot_type is None or empty string
#         if shot_type is None or shot_type.strip() == '':
#             queryset = TeamA.objects.all()  # Fetch all objects
#         else:
#             # Validate the shot type
#             if shot_type not in ['2P', '3P','FREE THROW','FOUL','TEAM REBOUND' , 'INBOUND','TURNOVER', 'SUBSTITUTION']:
#                 return Response({'message': 'Invalid shot type'}, status=status.HTTP_400_BAD_REQUEST)
            
#             queryset = TeamA.objects.filter(shot=shot_type)
        
#         # Get times and corresponding shot type
#         times_and_shot = queryset.exclude(time__isnull=True).values_list('shot', 'time')
        
#         # Convert queryset to list of dictionaries
#         response_data = [{'shot': shot, 'time': time} for shot, time in times_and_shot]
        
#         return Response(response_data)
    
# # TeamA delete
# class TeamADeleteView(APIView):
#     def delete(self, request, format=None):
#         try:
#             time = request.data.get('time')
#             if time is not None:
#                 queryset = TeamA.objects.filter(time=time)
#                 if queryset.exists():
#                     queryset.delete()
#                     return Response(status=status.HTTP_204_NO_CONTENT)
#                 else:
#                     return Response({"message": "No data found for the given time"}, status=status.HTTP_404_NOT_FOUND)
#             else:
#                 return Response({"message": "Time parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# # TeamB Insert and update 
# class TeamBCreateUpadateView(APIView):
#     def post(self, request, format=None):
#         time = request.data.get('time')

#         existing_entry = TeamB.objects.filter(time=time).first()

        
#         if existing_entry:
#             existing_entry.delete()

#         serializer = TeamBSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# # TeamB fetch data on the basis of shot 
# class TeamBFetchView(APIView):
#     def get(self, request, format=None):
#         shot_type = request.query_params.get('shot_type')
        
#         # Check if shot_type is None or empty string
#         if shot_type is None or shot_type.strip() == '':
#             queryset = TeamB.objects.all().order_by('time')  # Fetch all objects ordered by time
#         else:
#             # Validate the shot type
#             if shot_type not in ['2P', '3P','FREE THROW','FOUL','TEAM REBOUND' , 'INBOUND','TURNOVER', 'SUBSTITUTION']:
#                 return Response({'message': 'Invalid shot type'}, status=status.HTTP_400_BAD_REQUEST)
            
#             queryset = TeamB.objects.filter(shot=shot_type).order_by('time')
        
#         serializer = TeamBSerializer(queryset, many=True)
#         return Response(serializer.data)

# # TeamB fetch time fetch time on basis of shot 
# class TeamBTimeListView(APIView):
#     def get(self, request, format=None):
#         shot_type = request.query_params.get('shot_type')
        
#         # Check if shot_type is None or empty string
#         if shot_type is None or shot_type.strip() == '':
#             queryset = TeamB.objects.all()  # Fetch all objects
#         else:
#             # Validate the shot type
#             if shot_type not in ['2P', '3P','FREE THROW','FOUL','TEAM REBOUND' , 'INBOUND','TURNOVER', 'SUBSTITUTION']:
#                 return Response({'message': 'Invalid shot type'}, status=status.HTTP_400_BAD_REQUEST)
            
#             queryset = TeamB.objects.filter(shot=shot_type)
        
#         # Get times and corresponding shot type
#         times_and_shot = queryset.exclude(time__isnull=True).values_list('shot', 'time')
        
#         # Convert queryset to list of dictionaries
#         response_data = [{'shot': shot, 'time': time} for shot, time in times_and_shot]
        
#         return Response(response_data)
    
# # TeamB delete
# class TeamBDeleteView(APIView):
#     def delete(self, request, format=None):
#         try:
#             time = request.data.get('time')
#             if time is not None:
#                 queryset = TeamB.objects.filter(time=time)
#                 if queryset.exists():
#                     queryset.delete()
#                     return Response(status=status.HTTP_204_NO_CONTENT)
#                 else:
#                     return Response({"message": "No data found for the given time"}, status=status.HTTP_404_NOT_FOUND)
#             else:
#                 return Response({"message": "Time parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
            # return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)