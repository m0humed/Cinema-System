from django.db import models


from django.db.models.signals import  post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your models here.

# -- Movies  -- Guest -- Reservation

class Movie(models.Model):
    hall = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    date = models.DateField()

class Guest(models.Model):
    name = models.CharField(max_length=20 , null=False)  
    phone = models.CharField(max_length=20)

class Reservation(models.Model):
    movie = models.ForeignKey(Movie ,on_delete=models.CASCADE,related_name="Reservation")
    guest = models.ForeignKey(Guest ,on_delete=models.CASCADE,related_name="Reservation")


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def createToken(sender , instance , created , **kwargs):
    if created:
        Token.objects.create(user=instance)
