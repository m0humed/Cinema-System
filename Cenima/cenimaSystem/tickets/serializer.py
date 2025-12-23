from rest_framework import serializers
from tickets.models import Movie ,Guest , Reservation 


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model =Movie
        fields='__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model =Guest
        fields="__all__"

class ReservSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields=["pk" , "reservation_guest","name" , "phone"] 
        
        
        
        
