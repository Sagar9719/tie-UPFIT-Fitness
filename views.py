from django.shortcuts import render, redirect
from django.http import HttpResponse

def register(request):
    return render(request, 'tieup/register.html')


def login(request):
    return render(request, 'tieup/login.html')




def index(request):
    return render(request,'tieup/index.html')

def home(request):
    return render(request, 'tieup/home.html')

def profile(request):
    return render(request, 'tieup/profile.html')

def events(request):
    return render(request, 'tieup/events.html')







