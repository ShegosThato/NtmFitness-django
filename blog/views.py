from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = "blog-list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog-detail.html"
    context_object_name = 'post'


class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'new-comment.html'
    form_class = CommentForm

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = self.request.user.id
        initial['post'] = self.kwargs['post_id']
        return initial

    def get_success_url(self):
        post_id = self.object.post.id
        return reverse('blog:blog_detail', kwargs={'pk': post_id})
