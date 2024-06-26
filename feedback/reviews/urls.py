from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.ReviewView.as_view(), name='review-page'),
    path('reviews', view=views.ReviewListView.as_view(), name='review-list-page'),
    path('thankyou', view=views.ThankYouView.as_view(), name='thankyou-page'),
    path('reviews/favorite', view=views.FavoriteReviewView.as_view(), name='favorite-review-page'), # put this in front of the <int:pk> path, so this will be evaluated first
    path('reviews/<int:pk>', view=views.ReviewDetailView.as_view(), name='review-detail-page'),
]