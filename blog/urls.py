from django.conf.urls import url
from blog import views


app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)$', views.post, name='post'),

    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]
