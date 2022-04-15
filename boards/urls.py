from django.urls import path, re_path
from . import views

urlpatterns = [
    path('boards',views.boards, name='boards'),
    re_path(r'^boards/(?P<pk>\d+)/$',views.board_topics, name='board_topics'),
    re_path(r'^boards/(?P<pk>\d+)/new/$',views.new_topic, name='new_topic'),

]