from rest_framework import serializers
from .models import Housekeeper

class HousekeeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housekeeper
        fields = ['id', 'name', 'mobile', 'language', 'username', 'password', 'app_language']  # Match model fields

