from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date_posted = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='posts')
    tag = models.ManyToManyField('Tag', related_name='posts')
    

    def __str__(self):
        return self.title
    

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    posts = models.ManyToManyField(Post, related_name='tags')

    def __str__(self):
        return self.caption