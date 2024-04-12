from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.starting_page, name='starting-page'),
    path('posts', view=views.posts, name='posts-page'),
    path('posts/<slug:slug>', view=views.post_detail, name='post-detail-page'),
    path('plots', view=views.show_plot, name='plots-page'),
    path('plots2', view=views.plot_view, name='plots-page-2')

]