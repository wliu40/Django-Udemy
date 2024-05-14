from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views import View
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

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        current_review_id = self.object.id
        favorite_review = self.request.session.get('favorite_review')
        if str(current_review_id) == favorite_review:
            context['is_favorite_review'] = True
        else:
            context['is_favorite_review'] = False
        return context


class FavoriteReviewView(View):
    def post(self, request, *args, **kwargs):
        review_id = request.POST.get('review_id')
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/'+review_id)




