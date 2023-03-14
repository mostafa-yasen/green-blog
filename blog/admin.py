from django.contrib import admin
from blog.models import Blog
from blog.models import BlogPost


class BlogAdmin(admin.ModelAdmin):
    pass


class BlogPostAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
