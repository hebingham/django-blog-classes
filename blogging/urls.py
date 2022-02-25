# blogging/urls.py
from django.urls import path
from blogging.views import StubView
from blogging.views import PostListView
from blogging.views import PostDetailView
urlpatterns = [
    path('', PostListView.as_view(), name="blog_index"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="blog_detail"),
]