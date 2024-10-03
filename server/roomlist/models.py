from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100)
    is_paymaster = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100)
    modified_by = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.room_name
