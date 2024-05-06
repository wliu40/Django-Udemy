from django.shortcuts import render

# Create your views here.
def starting_page(request):
    return render(request, 'reviews/index.html')


def posts(request):
    return render(request, 'reviews/reviews.html')

