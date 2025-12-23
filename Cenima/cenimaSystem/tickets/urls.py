from django.urls import path  
from tickets import views

urlpatterns = [
    path('jsonrespons/' , views.no_rest_no_models ),
    path('jsonresponsmodel/' , views.no_rest_from_model ),
    path('jsonRestModel/' , views.VPS_Guest ),
]