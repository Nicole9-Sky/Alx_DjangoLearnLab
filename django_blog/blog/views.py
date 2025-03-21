from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from .models import Post 
from django.views.generic import ListView,  DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    
    
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    templates_name = "blog/post_form.html"
    fields = ["title", "content"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDetailView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog-home")
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("blog-home")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("blog-home")

@login_required
def profile(request):
    return render(request, "blog/profile.html")


def home(request):
    return render(request, 'blog/home.html')
