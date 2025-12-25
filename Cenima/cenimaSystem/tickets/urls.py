from django.urls import path  ,include
from tickets import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register("movies",views.ViewSets_Movie)

urlpatterns = [
    # start FBV
    path('FBV/jsonrespons/' , views.no_rest_no_models ),
    path('FBV/jsonresponsmodel/' , views.no_rest_from_model ),
    path('FBV/jsonRestModel/' , views.VPS_Guest ),
    path('FBV/jsonRestModelPK/<int:pk>' , views.VPS_PK ),
    path('FBV/MovieSearch',views.filterMovies),
    path('FBV/ComplexMovieSearch',views.complexFilterMovies),
    
    # Start CBV Class Based Model
    path('CBV/Get&SetMovies',views.CBV_Movies.as_view()),
    path('CBV/get&put&deleteMovie/<int:pk>',views.CBV_Movies_pk.as_view()),
    
    # Start Max Mixins_Reservations
    path('Mix/Get&SetReservations' , views.Mixins_Reservations.as_view()),
    path('Mix/Get&put&deleteReservations/<int:pk>' , views.Mixins_Reservations_pk.as_view()),
    
    # Start Genarics Mixins_Reservations
    path('Genaric/Get&SetReservations' , views.Genaric_Reservations.as_view()),
    path('Genaric/Get&put&deleteReservations/<int:pk>' , views.Genaric_Reservations_pk.as_view()),
    
    # Start ViewSets ruting
    path('Viewsets/AllInOne',include(routers.urls)),
]