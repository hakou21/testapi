from rest_framework import serializers
from .models import vicer

class vicerserializer(serializers.ModelSerializer):
    class Meta:
        model=vicer
        fields='__all__'