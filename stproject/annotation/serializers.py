from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from .models import Matches

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = '__all__'
    # def validate(self, data):
    #     instance = Matches(**data)
    #     try:
    #         instance.clean()  # This will raise a ValidationError if the data is invalid
    #     except DjangoValidationError as e:
    #         # Raise a DRF validation error with a custom message
    #         raise DRFValidationError({"detail": "Wrong player added in first five"})
    #     return data

