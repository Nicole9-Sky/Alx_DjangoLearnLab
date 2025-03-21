from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from .models import Post, Comment
from .forms import CommentForm 
from django.views.generic import ListView,  DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    
    
class PostDetailView(LoginRequiredMixin, UserPassesTestMixin,DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostCreateView(LoginRequiredMixin,  UserPassesTestMixin, CreateView):
    model = Post
    templates_name = "blog/post_form.html"
    fields = ["title", "content"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post-detail", pk=post.id)
    else:
        form = CommentForm()
    return render(request, "blog/add_comment.html", {"form": form})

@login_required
def edit_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post-detail", pk=post_id)
    else:
        form = CommentForm(instance=comment)
    return render(request, "blog/edit_comment.html", {"form": form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    comment.delete()
    return redirect("post-detail", pk=post_id)

    
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

@login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form})


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
