from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Tag
from .forms import CommentForm 
from django.views.generic import ListView,  DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
from django.db.models import Q
from .forms import SearchForm


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
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "blog/add_comment.html"
    form_class = CommentForm
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     return reverse("post-detail", kwargs={"pk": self.kwargs["post_id"]})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/edit_comment.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.post.id})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.post.id})

    
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


def search_posts(request):
    query = request.GET.get('query')
    results = Post.objects.filter(title__icontains=query) if query else []
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})


    if query:
        results = results.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)|
            Q(tags__name__icontains=query)
        ).distinct()
        
        return render(request, "blog/search_results.html", {'query': query, 'results': results})
    
    
def posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = post.objects.filter(tags=tag)
    return render(request, "blog/posts_by_tag.html", {"tag": tag, "posts": posts})