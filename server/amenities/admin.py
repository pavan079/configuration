# amenities/admin.py
from django.contrib import admin
from .models import Amenity

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('amenity_name', 'amenity_type', 'room_type', 'sort_key')
