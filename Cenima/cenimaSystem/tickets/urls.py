from django.urls import path  
from tickets import views

urlpatterns = [
    path('jsonresponsmodel/' , views.no_rest_no_models )
]