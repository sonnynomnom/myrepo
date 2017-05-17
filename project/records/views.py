from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from records.models import Post
from django.urls import reverse_lazy


# Create your views here.

class PostListView(ListView):

    model = Post

class PostDetailView(DetailView):

    model = Post

from django.views.generic.edit import CreateView

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'slug', 'image', 'content']

from django.views.generic.edit import UpdateView

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'slug', 'image', 'content']
    template_name_suffix = '_update_form'

from django.views.generic.edit import DeleteView

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('records:list_posts')
