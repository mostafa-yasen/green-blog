from django.urls import path
from blog.views import NewBlogView
from blog.views import UpdateBlogView


urlpatterns = [
    path("create/", NewBlogView.as_view(), name="new-blog"),
    path("<int:pk>/edit/", UpdateBlogView.as_view(), name="edit-blog"),
]
