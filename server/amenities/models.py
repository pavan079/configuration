# amenities/models.py
from django.db import models

class Amenity(models.Model):
    amenity_name = models.CharField(max_length=100)
    amenity_type = models.CharField(max_length=50)
    room_type = models.CharField(max_length=50)
    sort_key = models.IntegerField()

    def __str__(self):
        return self.amenity_name
