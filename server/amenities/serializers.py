# amenities/serializers.py
from rest_framework import serializers
from .models import Amenity

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'

    def validate(self, data):
        if 'amenity_name' not in data:
            raise serializers.ValidationError("Amenity name is required.")
        if 'amenity_type' not in data:
            raise serializers.ValidationError("Amenity type is required.")
        if 'room_type' not in data:
            raise serializers.ValidationError("Room type is required.")
        if 'sort_key' not in data:
            raise serializers.ValidationError("Sort key is required.")
        return data
