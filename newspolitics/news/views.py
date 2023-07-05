from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'flatpages/post_list.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context


class PostDetail(DetailView):
    model = Post
    ordering = 'title'
    template_name = 'flatpages/post_detail.html'
    context_object_name = 'post_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context
