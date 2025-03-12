from rest_framework import serializers
from .models import Sports

class SportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sports
        fields = '__all__'  # 또는 필요한 필드 지정