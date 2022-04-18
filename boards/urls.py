from django.urls import path, re_path
from . import views

urlpatterns = [
    path('boards',views.BoardListView.as_view(), name='boards'),
    re_path(r'^boards/(?P<pk>\d+)/$',views.board_topics, name='board_topics'),
    re_path(r'^boards/(?P<pk>\d+)/new/$',views.new_topic, name='new_topic'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    re_path(r'^boards/(?P<pk>\d+)/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='edit_post'),
    

]