from django.http.response import JsonResponse 
from rest_framework import status , filters 
from rest_framework.decorators import api_view # it is using with function based view
from .models import *
from .HttpRequestsMethods import *
from .serializer import GuestSerializer , MovieSerializer ,ReservSerializer
from rest_framework.response import Response
from rest_framework.views import APIView # it is using with class based views
from django.http import Http404
#1 Create your views here.
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
    

#2 model Data Default Django without Rest
def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests': list(data.values('name','phone'))
    }
    return JsonResponse(response)

# useing Rest and Models
#3 Function based view 

#3.1 Get And Post 
@api_view([Get , Post])
def VPS_Guest(request):
     # GET
    if request.method == Get:
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == Post:
        serializer = GuestSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
    

#3.2  GetByID , PUT , DELETE
@api_view([Get , Put  , Delete])
def VPS_PK(request , pk=1):
    try:
        guest = Guest.objects.get(pk = pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == Get:
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
   
    # Put
    elif request.method == Put:
        serializer = GuestSerializer(guest , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
    # Delete
    elif request.method == Delete:
        try :
            guest.delete()
            return Response("Deleted",status=status.HTTP_200_OK)
        except :
            return Response("Bad", status= status.HTTP_400_BAD_REQUEST)



#4 Class Based Views


#4.1 Get List , Post New 
class CBV_Movies(APIView):
    def get(self , request):
        try:
            movies = Movie.objects.all()
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movies , many = True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    def post(self , request):
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)


class CBV_Movies_pk(APIView):
    def get_Object(self , pk):
        try:
            return Movie.objects.get(pk = pk)
        except:
            raise Http404
    
    def get(self , request , pk):
        movie = self.get_Object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def put(self , request,pk):
        movie = self.get_Object(pk)
        print("="*50)
        print(movie.__str__)
        print("="*50)
        serializer = MovieSerializer(movie  , data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request,pk):
        movie = self.get_Object(pk)
        try :
            movie.delete()
            return Response("Deleted",status=status.HTTP_200_OK)
        except :
            return Response("Has problem during delete", status= status.HTTP_400_BAD_REQUEST)
