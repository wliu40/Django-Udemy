
import os
# Create your views here.
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = ['user_image']
    success_url = "/profiles"


