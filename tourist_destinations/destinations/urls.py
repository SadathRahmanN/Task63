from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('destinations/', views.destination_list, name='destination_list'),  # List of destinations
    path('login/', views.log_in, name='log_in'),  # Login page
    path('signup/', views.sign_up, name='sign_up'),  # Sign-up page
]
