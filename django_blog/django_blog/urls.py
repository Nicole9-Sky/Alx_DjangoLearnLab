"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog.views import register, profile, home, CommentCreateView, CommentUpdateView, CommentDeleteView
from blog.models import Comment, Post


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('blog.urls')),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', profile, name='profile'),
    
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('post/<int:post_id>/comments/<int:comment_id>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comments/<int:comment_id>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]
