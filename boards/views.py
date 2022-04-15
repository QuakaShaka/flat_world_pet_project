from unicodedata import name
from django.urls import path
from urllib import request
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.models import User

from boards.models import Board, Topic, Post

# Create your views here.
def boards(request):
    boards = Board.objects.all()

    return render(request, 'boards.html', {'boards': boards})

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)

    return render(request, 'topics.html', {'board': board})

def new_topic(request,pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()

        topic = Topic.objects.create(
            name=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

    return render(request, 'new_topic.html', {'board': board})

