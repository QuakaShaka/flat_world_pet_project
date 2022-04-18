from django.urls import path, re_path
from . import views

urlpatterns = [
    path('boards',views.boards, name='boards'),
    re_path(r'^boards/(?P<pk>\d+)/$',views.board_topics, name='board_topics'),
    re_path(r'^boards/(?P<pk>\d+)/new/$',views.new_topic, name='new_topic'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    re_path(r'^boards/(?P<pk>\d+)/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),


]