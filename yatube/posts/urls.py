from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group_posts, name='groups'),
    path('group_list.html', views.group_posts, name='groups'),
]

    # path('group/<slug:slug>/', views.group_posts)
