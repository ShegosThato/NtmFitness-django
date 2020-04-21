from django.urls import path
from .views import PostDetailView, PostListView, CommentCreateView

app_name = 'blog'

urlpatterns = [
    # /blog/
    path('', PostListView.as_view(), name='blog_list'),
    # /blog/pk/
    path('<int:pk>', PostDetailView.as_view(), name='blog_detail'),
    # /blog/pk/comment/
    path('<int:post_id>/comment', CommentCreateView.as_view(), name='new_comment')

]
