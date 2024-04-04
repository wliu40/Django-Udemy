from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request, 'blog/all-posts.html')

def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')


def coin_index(request):
    return render(request, 'blog/coin_index.html')


def plot_chart(request):
    sales_data = {
        'shopA': [
            {'date': '2023-03-01', 'sales': 100},
            {'date': '2023-03-02', 'sales': 150},
            {'date': '2023-03-03', 'sales': 120},
            # ... more data points for Shop A
        ],
        'shopB': [
            {'date': '2023-03-01', 'sales': 80},
            {'date': '2023-03-02', 'sales': 200},
            {'date': '2023-03-03', 'sales': 180},
            # ... more data points for Shop B
        ],
    }

    return render(request, 'blog/plot_chart.html', {'sales_data': sales_data})