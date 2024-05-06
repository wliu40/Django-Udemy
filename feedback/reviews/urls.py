from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.starting_page, name='starting-page'),
    path('posts', view=views.posts, name='posts-page'),
]