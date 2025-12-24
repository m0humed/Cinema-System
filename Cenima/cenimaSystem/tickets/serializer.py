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
    movie = MovieSerializer(read_only=True)
    guest = GuestSerializer(read_only=True)

    movie_id = serializers.PrimaryKeyRelatedField(
        write_only=True, source='movie', queryset=Movie.objects.all()
    )
    guest_id = serializers.PrimaryKeyRelatedField(
        write_only=True, source='guest', queryset=Guest.objects.all()
    )

    class Meta:
        model = Reservation
        fields = ['pk', 'movie', 'guest', 'movie_id', 'guest_id']




