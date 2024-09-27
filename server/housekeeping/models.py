from django.db import models

class Housekeeper(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    language = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    app_language = models.CharField(max_length=50, default="Default")

    def __str__(self):
        return self.name
    
