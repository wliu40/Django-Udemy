from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .models import Review

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thankyou'


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'


class ThankYouView(TemplateView):
    model = Review
    template_name = 'reviews/thankyou.html'
    context_object_name = 'review'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'

