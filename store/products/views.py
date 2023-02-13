from django.shortcuts import render



def home(request, pk=None):
    return render(request, 'home/home.html')