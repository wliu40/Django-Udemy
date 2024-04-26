from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=36)
    surname = models.CharField(max_length=36)

class Book(models.Model):
    title = models.CharField(max_length=36)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    rating = models.DecimalField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], max_digits=3, decimal_places=2)
    is_bestselling = models.BooleanField(default=False)

    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
