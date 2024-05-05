from django.contrib import admin

# Register your models here.

from .models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags', 'date_posted')
    list_display = ('title', 'date_posted', 'author')
    prepopulated_fields = {'slug': ('title',)}  

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
