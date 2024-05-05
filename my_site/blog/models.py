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
    image_name = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts', null=True)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title
