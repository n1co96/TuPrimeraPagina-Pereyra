from django.db import models
from django.contrib.auth.models import User

class Vino(models.Model):
    año= models.CharField(max_length=20)
    marca= models.CharField(max_length=20)
    cantidad= models.IntegerField()


    def __str__(self):
        return f'{self.marca} {self.año} {self.cantidad}'

# Create your models here.
