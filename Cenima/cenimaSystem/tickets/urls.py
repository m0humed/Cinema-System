from django.urls import path  
from tickets import views

urlpatterns = [
    path('FBV/jsonrespons/' , views.no_rest_no_models ),
    path('FBV/jsonresponsmodel/' , views.no_rest_from_model ),
    path('FBV/jsonRestModel/' , views.VPS_Guest ),
    path('FBV/jsonRestModelPK/<int:pk>/' , views.VPS_PK ),
    # Start CBV Class Based Model
    path('CBV/Get&SetMovies',views.CBV_Movies.as_view())
]