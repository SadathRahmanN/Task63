from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=200)
    weather = models.CharField(max_length=100)
    location = models.CharField(max_length=200)  # For state and district
    google_map_link = models.URLField()
    image = models.ImageField(upload_to='destinations/')
    description = models.TextField()

    def __str__(self):
        return self.name
