from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import myform, ReviewForm
from .models import Review

# Create your views here.
def starting_page(request):
    return render(request, 'reviews/index.html')


def posts(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data
            print(form.cleaned_data)
            review = Review(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                review=form.cleaned_data['review']
            )
            review.save()
            return HttpResponseRedirect('/thankyou')
    else:
        form = ReviewForm()
    return render(request, 'reviews/reviews.html', {'form': form})

def thankyou(request):
    return render(request, 'reviews/thankyou.html')