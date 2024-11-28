from django.db import models

# Create your models here.
class Park(models.Model):
    name = models.CharField(max_length=255)  
    description = models.TextField()  #description of the park
    latitude = models.FloatField()  
    longitude = models.FloatField() 
    
    def __str__(self):
        return self.name
