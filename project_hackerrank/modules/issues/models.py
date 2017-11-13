from django.db import models
import uuid


# Create your models here.
class Problemas(models.Model):
    id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length = 255, blank=True)
    instrucciones = models.CharField(max_length = 255, blank=True)
    timestamp = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.pregunta