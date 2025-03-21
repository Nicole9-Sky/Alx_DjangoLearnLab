from django.urls import path
from .views import register, user_login, user_logout, profile
from django.contrib.auth import views as auth_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from .views import add_comment, edit_comment, delete_comment

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path('posts/<int:post_id>/comments/new/', add_comment, name='add_comment'),
    path('comments/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
    

