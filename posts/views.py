from django.views.generic import (
UpdateView,
DeleteView,
ListView,
DetailView,
CreateView
)
from .models import Post
from django.urls import reverse_lazy

class PostUpdateView(UpdateView):
	model = Post
	template_name = "posts/edit.html"
	fields = [
		"title", "subtitle", "body", "author"]

class PostDeleteView(DeleteView):
	template_name = "posts/delete.html"
	model = Post
	success_url = reverse_lazy("list")

class PostListView(ListView):
	template_name = "posts/list.html"
	model = Post
	
class PostDetailView(DetailView):
	template_name = "posts/detail.html"
	model = Post

class PostCreateView(CreateView):
	template_name = "posts/new.html"
	model = Post
	fields = ["title", "subtitle", "body", "author"]
	# success_url = reverse("list")
