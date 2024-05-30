from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Matches
from .serializers import MatchSerializer

class CreateMatch(APIView):
    def post(self, request, format=None):
        video_link = request.data.get('video_link')
        match = Matches.objects.filter(video_link=video_link).first()

        if match:
            serializer = MatchSerializer(match, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = MatchSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateMatch(APIView):
    def put(self, request, format=None):
        match_id = request.query_params.get('match_id')
        
        try:
            existing_entry = Matches.objects.get(match_id=match_id)
        except Matches.DoesNotExist:
            return Response({"message": "No data found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MatchSerializer(existing_entry, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteMatch(APIView):
    def delete(self, request,format=None):
        try:
            match_id = request.data.get("match_id")
            if match_id is not None:
                    queryset = Matches.objects.filter(match_id=match_id)
                    if queryset.exists():
                        queryset.delete()
                        return Response(
                             {"message": "Match deleted"},
                            status=status.HTTP_204_NO_CONTENT)
                    else:
                        return Response(
                            {"message": "No data found"},
                            status=status.HTTP_404_NOT_FOUND,
                        )
            else:
                return Response(
                    {"message": "match_id parameter is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



# class MatchView(APIView):
#     def post(self, request, format=None):
#         match_id = request.data.get('match_id')

#         if match_id:
#             try:
#                 existing_entry = Matches.objects.get(match_id=match_id)
#                 serializer = MatchSerializer(existing_entry, data=request.data, partial=True)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data, status=status.HTTP_200_OK)
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             except Matches.DoesNotExist:
#                 return Response({"message": "No data found for the given match_id"}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             serializer = MatchSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)