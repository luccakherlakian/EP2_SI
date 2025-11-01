from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


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

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post           
            comment.autor = request.user 
            comment.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'add_comment_to_post.html', {'form': form})