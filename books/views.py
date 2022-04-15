from django.urls import path
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def forum(request):
    return render(request, 'forum.html')