from .models import Post, PostCategory, Comment, Category
from django.contrib import admin

# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Category)