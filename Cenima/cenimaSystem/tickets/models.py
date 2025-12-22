from django.db import models

# Create your models here.

# -- Movies  -- Guest -- Reservation

class Movie(models.Model):
    hall = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    date = models.DateField()
    
    


class Guest(models.Model):
    name = models.CharField(max_length=20 , null=False)  
    Phone = models.CharField(max_length=20)

class Reservation(models.Model):
    movie = models.ForeignKey(Movie ,on_delete=models.CASCADE,related_name="reservation_movie")
    guest = models.ForeignKey(Guest ,on_delete=models.CASCADE,related_name="reservation_guest")



