from rest_framework import serializers
from .models import *
from AuthUser.serializer import UserSerializer


class GarageSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user_id.id', read_only=True)

    class Meta:
        model = Garage
        fields = ['name', 'description', 'latitude', 'longitude', 'user_id']


class EngineerSerializer(serializers.ModelSerializer):
    garage_id = GarageSerializer()

    class Meta:
        model = Engineer
        fields = ['id', 'username', 'phone', 'description', 'garage_id']
