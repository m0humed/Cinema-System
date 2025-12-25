from django.http.response import JsonResponse 
from rest_framework import status , filters , generics , mixins  , viewsets
from rest_framework.decorators import api_view # it is using with function based view
from .models import *
from .HttpRequestsMethods import *
from .serializer import GuestSerializer , MovieSerializer ,ReservSerializer
from rest_framework.response import Response
from rest_framework.views import APIView # it is using with class based views
from django.http import Http404
import re
from rest_framework.authentication import BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly

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

#4.2 Get by ID , Put , Delete 
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


#5 using generic and Mixins With Reservations
#5.1 Get List , Post New 
class Mixins_Reservations(mixins.CreateModelMixin , mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self , request):
        return self.list(request)
    def post(self , request):
        return self.create(request)
    

#5.2 Get by ID , Put , Delete 

class Mixins_Reservations_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self , request , pk):
        return self.retrieve(pk)
    def put(self , request , pk):
        return self.update(request)
    def delete(self , request , pk):
        return self.destroy(pk)
    

#6 Generics
#6.1 Get List , Post New 
class Genaric_Reservations(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


#6.2 Get by ID , Put , Delete 

class Genaric_Reservations_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


#7 ViewSets All in one
class ViewSets_Movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
#8.1 filter movies
@api_view([Get])
def filterMovies(request):
    try:
        filterd = Movie.objects.filter(
            name = request.data['name'],
            hall = request.data['hall']
        )
        serialized = MovieSerializer(filterd , many=True )
        return Response(serialized.data , status=status.HTTP_200_OK)
    except:
        return Response(serialized.data , status=status.HTTP_400_BAD_REQUEST)

#8.2 complex filter
@api_view([Get])
def complexFilterMovies(request):
    name = request.query_params.get('name', '').strip()
    hall = request.query_params.get('hall', '').strip()
    if not name and not hall:
        return Response({"detail": "Provide 'name' or 'hall' query parameter."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        qs = Movie.objects.all()
        if name:
            pattern = r'.*' + re.escape(name) + r'.*'
            qs = qs.filter(name__iregex=pattern)
        if hall:
            pattern = r'.*' + re.escape(hall) + r'.*'
            qs = qs.filter(hall__iregex=pattern)
        serialized = MovieSerializer(qs, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"detail": "Bad request", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)




