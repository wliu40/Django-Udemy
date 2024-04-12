from django.shortcuts import render
from datetime import date
import json
import datetime

my_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


# pay attention to those functions and the parameters they take
# the index page will show the first 3 posts, in the index.html file you can see we had a for loop that iterated over the posts
# and displayed them, we passed the posts as a parameter to the render function

# the posts page will show all the posts, we passed all the posts to the render function
# inside the all-posts.html file we had a for loop that iterated over the posts and displayed them

# the post detail page will show the details of a single post, we passed the identified post to the render function

def starting_page(request):
    return render(request, 'blog/index.html', {'posts': my_posts[:3]})


def posts(request):
    return render(request, 'blog/all-posts.html', {'posts': my_posts})


def post_detail(request, slug):
    identified_post = list(filter(lambda x: x['slug'] == slug, my_posts))
    return render(request, 'blog/post-detail.html', {'post': 
                                                     identified_post[0]})

def show_plot(request):
    # Simulated data (replace with your actual data retrieval logic)
    data = [
            {'user': 'User1', 'login_time': '2023-06-01 09:15:00', 'login_status': 'Success', 'height': 1},
            {'user': 'User2', 'login_time': '2023-06-01 09:30:00', 'login_status': 'Fail', 'height': 2},
            {'user': 'User1', 'login_time': '2023-06-02 10:45:00', 'login_status': 'Success', 'height': 1},
            {'user': 'User3', 'login_time': '2023-06-02 11:00:00', 'login_status': 'Success', 'height': 3},
            {'user': 'User2', 'login_time': '2023-06-03 11:20:00', 'login_status': 'Success', 'height': 2},
            {'user': 'User4', 'login_time': '2023-06-03 12:10:00', 'login_status': 'Fail', 'height': 4},
            {'user': 'User3', 'login_time': '2023-06-04 13:30:00', 'login_status': 'Success', 'height': 3},
            {'user': 'User4', 'login_time': '2023-06-04 14:00:00', 'login_status': 'Success', 'height': 4},

        ]


    format_code = "%Y-%m-%d %H:%M:%S"
    # Convert login_time to timestamp format
    for item in data:
        x = datetime.datetime.strptime(item['login_time'], format_code)       
        item['login_time'] =  x.timestamp() * 1000
        item['height'] = item['height']


    # Convert data to JSON format
    json_data = json.dumps(data)

    # Render the template with the data
    return render(request, 'blog/plot_test.html', {'data': json_data})


def plot_view(request):
    x = ['2020-01-23 10:12:21', '2020-01-23 10:20:10', '2020-01-25 10:20:10']
    y = [20, 30, 15]
    
    return render(request, 'blog/plot_test_3.html', {'x': x, 'y': y})



    # x = ['2020-01-23 10:12:21', '2020-01-23 10:20:10', '2020-01-25 10:20:10']
    # y = [20, 30, 15]
    
    # data = {
    #     'x': x,
    #     'y': y
    # }
    
    # return render(request, 'blog/plot_test_3.html', {'data': json.dumps(data)})