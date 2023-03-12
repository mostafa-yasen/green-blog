from django.forms import BaseModelForm
from django.http import HttpResponse
from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.views.generic import CreateView, TemplateView, UpdateView

from blog.forms import BlogForm, BlogPostForm
from blog.models import Blog, BlogPost
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from typing import Dict, Any


class NewBlogView(CreateView):
    form_class = BlogForm
    template_name = "blog_settings.html"

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.owner = self.request.user
        blog_obj.slug = slugify(blog_obj.title)
        blog_obj.save()
        return HttpResponseRedirect(reverse("home"))

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if Blog.objects.filter(owner=user).exists():
            return HttpResponseForbidden(
                "You can not create more than one blogs per account"
            )

        return super(NewBlogView, self).dispatch(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super(HomeView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if Blog.objects.filter(owner=self.request.user).exists():
                ctx["has_blog"] = True
                ctx["blog"] = Blog.objects.get(owner=self.request.user)
        return ctx


class UpdateBlogView(UpdateView):
    form_class = BlogForm
    template_name = "blog_settings.html"
    success_url = "/"
    model = Blog

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateBlogView, self).dispatch(request, *args, **kwargs)


class NewBlogPost(CreateView):
    form_class = BlogPostForm
    template_name = "blog_post.html"
    success_url = "/"
    model = BlogPost

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        blog_post = form.save(commit=False)
        blog_post.blog = Blog.objects.get(owner=self.request.user)
        blog_post.slug = slugify(blog_post.title)
        blog_post.save()
        return HttpResponseRedirect(reverse("home"))
