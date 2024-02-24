from rest_framework import serializers
from .models import TeamA_Q1

class TeamA_Q1Serializer(serializers.ModelSerializer):
    class Meta:
        model = TeamA_Q1
        fields = '__all__'