from django.views.generic import ListView, DetailView
from .models import Post, Image
from taggit.models import Tag

class TaggedPostListView(ListView):
    model = Post
    template_name = 'list.html'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))

class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'
    context_object_name = 'post'

