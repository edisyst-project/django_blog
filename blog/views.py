from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import redirect

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

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
        return redirect('blog-home')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

