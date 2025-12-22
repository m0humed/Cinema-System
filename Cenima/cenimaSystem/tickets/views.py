from django.shortcuts import render
from django.http.response import JsonResponse
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
    
  








