from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import myform

# Create your views here.
def starting_page(request):
    return render(request, 'reviews/index.html')


def posts(request):
    if request.method == 'POST':
        form = myform(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data
            print(form.cleaned_data)
            return HttpResponseRedirect('/thankyou')
    else:
        form = myform()
        return render(request, 'reviews/reviews.html', {'form': form})

def thankyou(request):
    return render(request, 'reviews/thankyou.html')