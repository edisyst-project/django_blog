from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



def post_list(request):
    sort_by = request.GET.get('sort', 'date_posted')  # Imposta il parametro di ordinamento, default è 'date_posted'
    order = request.GET.get('order', 'desc')  # Imposta l'ordine, default è 'desc'

    if sort_by == 'title':
        if order == 'asc':
            posts = Post.objects.all().order_by('title')
        else:
            posts = Post.objects.all().order_by('-title')
    else:  # Ordina per data
        if order == 'asc':
            posts = Post.objects.all().order_by('date_posted')
        else:
            posts = Post.objects.all().order_by('-date_posted')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'sort_by': sort_by,
        'order': order
    }

    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user  # Non essendoci autenticazione, potresti voler cambiare questa riga
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Crea Post'})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Modifica Post'})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post, 'title': 'Elimina Post'})



