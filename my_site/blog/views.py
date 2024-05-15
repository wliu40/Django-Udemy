
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404



# pay attention to those functions and the parameters they take
# the index page will show the first 3 posts, in the index.html file you can see we had a for loop that iterated over the posts
# and displayed them, we passed the posts as a parameter to the render function

# the posts page will show all the posts, we passed all the posts to the render function
# inside the all-posts.html file we had a for loop that iterated over the posts and displayed them

# the post detail page will show the details of a single post, we passed the identified post to the render function

def starting_page(request):
    try:
        my_posts = list(Post.objects.all().values().order_by('-date')[:3])  # only show the first 3 posts
        return render(request, 'blog/index.html', {'posts': my_posts[:3]})
    except:
        return Http404('No posts found')

def posts(request):
    try:
        my_posts = list(Post.objects.all().values())
        return render(request, 'blog/all-posts.html', {'posts': my_posts})
    except:
        return Http404('No posts found')

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {'post': 
                                                     identified_post})


