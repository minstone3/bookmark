from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import *
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'


class BookmarkDetailView(DetailView):
    model = Bookmark
    success_url = reverse_lazy('list')
    template_name_suffix = '_detail'


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
