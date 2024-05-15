from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    
    

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200, null=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date_posted = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True) # this will uploaded to MEDIA_ROOT/images
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts', null=True)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.user_name