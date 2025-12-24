from django.urls import path  
from tickets import views

urlpatterns = [
    # start FBV
    path('FBV/jsonrespons/' , views.no_rest_no_models ),
    path('FBV/jsonresponsmodel/' , views.no_rest_from_model ),
    path('FBV/jsonRestModel/' , views.VPS_Guest ),
    path('FBV/jsonRestModelPK/<int:pk>' , views.VPS_PK ),
    
    # Start CBV Class Based Model
    path('CBV/Get&SetMovies',views.CBV_Movies.as_view()),
    path('CBV/get&put&deleteMovie/<int:pk>',views.CBV_Movies_pk.as_view()),
    
    # Start Max Mixins_Reservations
    path('Mix/Get&SetReservations' , views.Mixins_Reservations.as_view()),
    path('Mix/Get&put&deleteReservations/<int:pk>' , views.Mixins_Reservations_pk.as_view()),
    
]