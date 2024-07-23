from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

class MessageBoard(ListView):
    model = Post
    template_name = 'message_board/board.html'
    context_object_name = 'all_posts_list'

def view_post(request,slug):
    post = get_object_or_404(Post.objects, slug=slug)
    return render(request,
                'message_board/post.html',
                {
                    "post":post,
                })

def new_post(request):
    if request.method == 'POST':
        new_post= PostForm(data=request.POST)
        if new_post.is_valid:
            post= new_post.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request,f'New post created')
            return HttpResponseRedirect(reverse('view_post', args=[post.slug]))
    else:
        new_post = PostForm()
    return render (
        request,
        'message_board/new_post.html',
        {
            'new_post': new_post
        },
    )