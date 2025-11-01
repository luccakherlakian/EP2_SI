from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    context_object_name = 'posts' 

    queryset = Post.objects.all().order_by('-data_postagem')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    context_object_name = 'post' 

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm 
    template_name = 'post_form.html'

    success_url = reverse_lazy('post_list') 

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    context_object_name = 'post' 

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    context_object_name = 'post'

    success_url = reverse_lazy('post_list')