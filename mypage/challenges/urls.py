
from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name='index'),
    path("<int:num_month>", view=views.monthly_challenge_by_number),
    path("<str:month>", view=views.monthly_challenge, name='month-challenge'),
    ]