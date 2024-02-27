from rest_framework import serializers
from .models import TeamA

class TeamASerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamA
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {key: value for key, value in data.items() if value is not None}