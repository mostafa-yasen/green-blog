from django.contrib import admin
from blog.models import Blog
from blog.models import BlogPost


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass
