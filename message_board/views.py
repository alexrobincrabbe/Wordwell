from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView
from .models import Post
from .forms import PostForm, ReplyForm
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
            try:
                post= new_post.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request,f'New post created')
                return HttpResponseRedirect(reverse('view_post', args=[post.slug]))
            except ValueError as e: 
                pass
    else:
        new_post = PostForm()
    return render (
        request,
        'message_board/new_post.html',
        {
            'new_post': new_post
        },
    )

def edit_post(request, slug):
    if request.method == 'POST':
        post= get_object_or_404(Post.objects, slug=slug)
        edit_post_form = PostForm(data=request.POST, instance=post)
        if edit_post_form.is_valid:
            try:
                edit_post = edit_post_form.save(commit=False)
                edit_post.author = request.user
                edit_post.save()
                messages.success(request,f'Post updated')
                slug=post.slug
                return HttpResponseRedirect(reverse('view_post', args=[slug]))
            except ValueError as e: 
                pass
    else:
        post= get_object_or_404(Post.objects, slug=slug)
        edit_post_form = PostForm(instance=post)
    return render (
        request,
        'message_board/new_post.html',
        {
        'new_post': edit_post_form
        },
    )

def new_reply(request, slug):
    post = get_object_or_404(Post.objects, slug=slug)
    if request.method == 'POST':
        new_reply= ReplyForm(data=request.POST)
        if new_reply.is_valid:
                reply= new_reply.save(commit=False)
                reply.author = request.user
                reply.original_post = post
                reply.save()
                messages.success(request,f'Reply created')
                return HttpResponseRedirect(reverse('view_post', args=[slug]))
    else:
        new_reply = ReplyForm()
    return render (
        request,
        'message_board/reply.html',
        {
            'new_reply': new_reply,
            'post':post,
        },
    )
