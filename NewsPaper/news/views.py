from django.shortcuts import render
from django.views.generic import ListView
from news.models import Post


def home(request):
    return render(request, 'home.html')


class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['posts_exists'] = Post.objects.all().exists()
    #
    #     return context

