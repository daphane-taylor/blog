from django.views.generic import (
UpdateView,
DeleteView,
ListView,
DetailView,
CreateView
)
from .models import Post, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)

class PostCreateView(LoginRequiredMixin, CreateView):
	template_name = "posts/new.html"
	model = Post
	fields = ["title", "subtitle", "body", "status"]

	def form_valid(self, form):
		form.instance.author = self.request.user
		# form.instance.status = Status.objects.get(name="Published")
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	template_name = "posts/edit.html"
	fields = [
		"title", "subtitle", "body", "status"]

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	template_name = "posts/delete.html"
	model = Post
	success_url = reverse_lazy("list")

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

class PostListView(ListView):
	template_name = "posts/list.html"
	model = Post

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		Published = Status.objects.get(name="Published")
		context["post_list"] = (
			Post.objects.filter(status=Published)
			.order_by("-created_on").reverse()
		)
		return context
	
class DraftPostListView(LoginRequiredMixin, ListView):
	template_name = "posts/list.html"
	model = Post

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		Draft = Status.objects.get(name="Draft")
		context["post_list"] = (
			Post.objects.filter(status=Draft)
			.order_by("-created_on").reverse()
		)
		return context

class ArchivedPostListView(LoginRequiredMixin, ListView):
	template_name = "posts/list.html"
	model = Post	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		Archived = Status.objects.get(name="Archived")
		context["post_list"] = (
			Post.objects.filter(status=Archived)
			.order_by("-created_on").reverse()
		)
		return context
	
class PostDetailView(DetailView):
	template_name = "posts/detail.html"
	model = Post

