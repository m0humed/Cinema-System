from django.shortcuts import render
from django.http.response import JsonResponse 
from rest_framework import status , filters 
from rest_framework.decorators import api_view 
from .models import *
from .HttpRequestsMethods import *
from .serializer import GuestSerializer , MovieSerializer ,ReservSerializer
from rest_framework.response import Response
# Create your views here.
def no_rest_no_models(request):
    guests =  [
                {
                    "id": 1,
                    "name": "Ahmed Hassan",
                    "email": "ahmed.hassan@example.com",
                    "phone": "+20 101 234 5678",
                    "status": "Confirmed",
                    "guestsCount": 2,
                    "checkIn": False
                },
                {
                    "id": 2,
                    "name": "Sara Mohamed",
                    "email": "sara.mohamed@example.com",
                    "phone": "+20 109 876 5432",
                    "status": "Pending",
                    "guestsCount": 1,
                    "checkIn": False
                },
                {
                    "id": 3,
                    "name": "Omar Ali",
                    "email": "omar.ali@example.com",
                    "phone": "+20 122 345 6789",
                    "status": "Confirmed",
                    "guestsCount": 3,
                    "checkIn": True
                },
                {
                    "id": 4,
                    "name": "Mona Youssef",
                    "email": "mona.youssef@example.com",
                    "phone": "+20 115 456 7890",
                    "status": "Cancelled",
                    "guestsCount": 0,
                    "checkIn": False
                },
                {
                    "id": 5,
                    "name": "Khaled Mahmoud",
                    "email": "khaled.mahmoud@example.com",
                    "phone": "+20 100 987 6543",
                    "status": "Confirmed",
                    "guestsCount": 1,
                    "checkIn": False
                }
        ]
    return JsonResponse(guests , safe=False)
    

# model Data Default Django without Rest
def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests': list(data.values('name','Phone'))
    }
    return JsonResponse(response)

# useing Rest and Models
# Function based view 
# Get And 
@api_view([Get , Post])
def VPS_Guest(request):
     # GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = GuestSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
        






