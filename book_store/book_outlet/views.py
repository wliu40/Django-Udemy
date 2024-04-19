from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def book_detail(request, slug):
    return render(request, 'book_detail.html')

