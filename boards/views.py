from django.urls import path
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

from boards.models import Board

# Create your views here.
def boards(request):
    boards = Board.objects.all()

    return render(request, 'boards.html', {'boards': boards})

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)

    return render(request, 'topics.html', {'board': board})
