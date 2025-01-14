from django.shortcuts import render
from .models import Destination

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/destination_list.html', {'destinations': destinations})

def home(request):
    return render(request, 'destinations/home.html')