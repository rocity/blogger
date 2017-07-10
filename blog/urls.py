from django.conf.urls import url
from blog import views


app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)$', views.post, name='post'),

    url(r'^categories/$', views.categories, name='categories'),

    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboard/posts/(?P<post_status>\d+)', views.dashboard_my_posts, name='dashboard_my_posts_filtered'),
    url(r'^dashboard/posts/', views.dashboard_my_posts, name='dashboard_my_posts'),
    url(r'^dashboard/post/create/', views.dashboard_create_post, name='dashboard_create_post'),
]
