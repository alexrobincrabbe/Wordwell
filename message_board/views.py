from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView
from .models import Post,Reply
from .forms import PostForm, ReplyForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.db.models import OuterRef, Subquery
from django.db.models import Case, When

# Create your views here.

class MessageBoard(ListView):
    '''
    Paginated view of all posts
    annotates number of replies and time of last reply to each post
    Sorts posts by my reply date, or create date if there are no replies
    '''
    model = Post
    template_name = 'message_board/board.html'
    context_object_name = 'all_posts_list'
    paginate_by = 5
    def get_queryset(self, *args, **kwargs): 
        messages = Reply.objects.filter(original_post=OuterRef("pk")).order_by("-created_on")
        # Get create date of most recent reply to pot
        latest_reply = Subquery(messages.values('created_on')[:1])
        posts=Post.objects.filter(id=OuterRef('id'))
        # Get create date of post as subquery
        no_reply = Subquery(posts.values('created_on'))
        all_posts_list = Post.objects
        all_posts_list=all_posts_list.annotate(number_of_replies = Count('replies'))
        # Sort posts by latest reply, or date of post if there are no replies
        all_posts_list = all_posts_list.annotate(latest_reply = Case(When(number_of_replies=0, then = no_reply),When(number_of_replies__gte=1, then = latest_reply)))
        queryset = all_posts_list.order_by('-latest_reply', '-created_on')
        return queryset


def view_post(request,slug):
    post = get_object_or_404(Post.objects, slug=slug)
    return render(request,
                'message_board/view_post.html',
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
                return HttpResponseRedirect(reverse('message_board'))
            except ValueError as e: 
                pass
    else:
        new_post = PostForm()
    return render (
        request,
        'message_board/new_post.html',
        {
            'new_post': new_post,   
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
        'message_board/edit_post.html',
        {
        'new_post': edit_post_form,
        'post': post,
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
        'message_board/new_reply.html',
        {
            'new_reply': new_reply,
            'post':post,
        },
    )

def delete_post(request, slug):
    post=get_object_or_404(Post.objects, slug=slug)
    if request.user==post.author:
        post.delete()
        messages.success(request, 'Post deleted')
    else:
        messages.error(request, 'Permission denied')
    return HttpResponseRedirect('/board')

def edit_reply(request, slug, comment_id):
    if request.method == 'POST':
        post= get_object_or_404(Post.objects, slug=slug)
        reply = get_object_or_404(Reply.objects, id=comment_id)
        edit_reply_form = ReplyForm(data=request.POST, instance=reply)
        if edit_reply_form.is_valid:
            try:
                edit_reply = edit_reply_form.save(commit=False)
                edit_reply.author = request.user
                edit_reply.save()
                messages.success(request,f'Reply updated')
                slug=post.slug
                return HttpResponseRedirect(reverse('view_post', args=[slug]))
            except ValueError as e: 
                pass
    else:
        post= get_object_or_404(Post.objects, slug=slug)
        reply = get_object_or_404(Reply.objects, id=comment_id)
        edit_reply_form = ReplyForm(instance=reply)
    return render (
        request,
        'message_board/edit_reply.html',
        {
        'edit_reply_form': edit_reply_form,
        'post': post,
        'reply': reply,
        },
    )

def delete_reply(request, slug, reply_id):
    reply=get_object_or_404(Reply.objects, id=reply_id)
    if request.user==reply.author:
        reply.delete()
        messages.success(request, 'Reply deleted')
    else:
        messages.error(request, 'Permission denied')
    return HttpResponseRedirect(reverse('view_post', args=[slug]))