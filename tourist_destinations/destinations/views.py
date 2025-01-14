from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Destination

# Home View
def home(request):
    return render(request, 'destinations/home.html')

# Destination List View
def destination_list(request):
    destinations = Destination.objects.all()  # Fetch all destinations from the database
    return render(request, 'destinations/destination_list.html', {'destinations': destinations})

# Sign Up View
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to home or any other page
    else:
        form = UserCreationForm()
    return render(request, 'destinations/sign_up.html', {'form': form})

# Login View
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home or any other page
    else:
        form = AuthenticationForm()
    return render(request, 'destinations/log_in.html', {'form': form})
