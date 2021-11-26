from typing import List
from django.http import request
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('filter') == 'Женский':
            context['object_list'] = Post.objects.filter(sex_k="Женский")
        elif self.request.GET.get('filter') == 'Мужской':
            context['object_list'] = Post.objects.filter(sex_k="Мужской")
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BLogCreateView(CreateView):
    model =Post
    template_name = 'post_new.html'
    fields =['title','img','sex_k', 'body' ]

class BlogUpdateView(UpdateView):
    model =Post
    template_name = 'post_edit.html'
    fields =['title','img', 'sex_k', 'body']

class BlogDeleteView(DeleteView):
    model =Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')