from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

month_dict = {'january': "Eat no meat for the entire month",
              'february': "Walk for at least 20 minutes every day",
              'march': "Learn Django for at least 20 minutes every day",}

def monthly_challenge_by_number(request, num_month):
    months = list(month_dict.keys())
    if num_month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[num_month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    #return render(request, "challenges/challenge.html")
    return HttpResponse(month_dict[month])
