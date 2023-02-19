from django.urls import path
from blog.views import NewBlogView


urlpatterns = [path("create/", NewBlogView.as_view(), name="new-blog")]
