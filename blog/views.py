from django.contrib import messages
from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import Post, Tag, Comment
from .forms import CommentForm


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



def post_list(request):
    """
    Visualizza la lista di post con funzionalità di ricerca, filtro per tag e ordinamento.
    """
    posts = Post.objects.all()
    tags = Tag.objects.all()

    tag_filter = request.GET.get('tag')
    if tag_filter:
        posts = posts.filter(tags__id=tag_filter)

    query = request.GET.get('q')
    if query:
        posts = posts.filter(title__icontains=query)

    # Ordinamento
    sort = request.GET.get('sort', 'date_desc')
    if sort == 'title_asc':
        posts = posts.order_by('title')
    elif sort == 'title_desc':
        posts = posts.order_by('-title')
    elif sort == 'date_asc':
        posts = posts.order_by('date_posted')
    else:
        posts = posts.order_by('-date_posted')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'tags': tags,
        'sort': sort,
        'selected_tag': tag_filter,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    """
    Visualizza i dettagli di un singolo post, inclusi i commenti e il form per aggiungere un nuovo commento.
    """
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
    """
    Crea un nuovo post. Se il form è valido, salva il post nel database e reindirizza alla lista dei post.
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()  # Necessario per salvare i tag ManyToMany
            messages.success(request, 'Post creato con successo!')
            return redirect('post-list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_update(request, pk):
    """
    Aggiorna un post esistente. Se il form è valido, salva le modifiche e reindirizza alla lista dei post.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post aggiornato con successo!')
            return redirect('post-list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

def post_delete(request, pk):
    """
    Elimina un post esistente e reindirizza alla lista dei post.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post eliminato con successo!')
        return redirect('post-list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post, 'title': 'Elimina Post'})



