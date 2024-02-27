from rest_framework import serializers
from .models import TeamA

class TeamASerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamA
        fields = '__all__'