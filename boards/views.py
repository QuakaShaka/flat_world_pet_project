from unicodedata import name
from django.urls import path
from urllib import request
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import NewTopicForm
from django.contrib.auth.decorators import login_required

from boards.models import Board, Topic, Post

# Create your views here.
def boards(request):
    boards = Board.objects.all()

    return render(request, 'boards.html', {'boards': boards})

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)

    return render(request, 'topics.html', {'board': board})

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user  # <- here
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user  # <- and here
            )
            return redirect('board_topics', pk=board.pk) 
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})

def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    return render(request, 'topic_posts.html', {'topic': topic})
