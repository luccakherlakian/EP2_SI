from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-data_postagem')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        novo_titulo = request.POST.get('titulo')
        novo_conteudo = request.POST.get('conteudo')

        Post.objects.create(
            titulo=novo_titulo,
            conteudo=novo_conteudo
        )

        return redirect('post_list')

    return render(request, 'post_form.html')

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.titulo = request.POST.get('titulo')
        post.conteudo = request.POST.get('conteudo')
        post.save()

        return redirect('post_detail', pk=post.pk)

    return render(request, 'post_form.html', {'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete() 
        return redirect('post_list')

    return render(request, 'post_confirm_delete.html', {'post': post})