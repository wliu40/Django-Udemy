from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string

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
    return render(request, "challenges/challenge.html", {'month_name': month, 'month_challenge': month_dict[month]})


def index(request):
    list_items = ""
    months = list(month_dict.keys())
    ret = render(request, "challenges/index.html", {'months': months})
    return ret
