'''
Message Board views:
- MessageBoard (class based view)
- view_post
- new_post
- edit_post
- delete_post
- new_reply
- edit_reply
- delete_reply
'''
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.db.models import OuterRef, Subquery
from django.db.models import Case, When
from django.contrib.auth.decorators import login_required
from .models import Post, Reply
from .forms import PostForm, ReplyForm


class MessageBoard(ListView):
    '''
    Paginated view of all posts
    annotates number of replies and time of last reply to each post
    Sorts posts by my reply date, or create date if there are no replies
    '''
    model = Post
    template_name = 'message_board/board.html'
    context_object_name = 'all_posts_list'
    paginate_by = 10
    # Order by most recent reply create date, or the create date of the post
    # if there are no replies

    def get_queryset(self, *args, **kwargs):
        replies = Reply.objects.filter(
            original_post=OuterRef("pk")).order_by("-created_on")
        # Get create date of most recent reply to pot
        latest_reply = Subquery(replies.values('created_on')[:1])
        posts = Post.objects.filter(id=OuterRef('id'))
        # Get create date of post as subquery
        no_reply = Subquery(posts.values('created_on'))
        all_posts_list = Post.objects
        all_posts_list = all_posts_list.annotate(
            number_of_replies=Count('replies'))
        # Sort posts by latest reply, or date of post if there are no replies
        all_posts_list = all_posts_list.annotate(
            latest_reply=Case(
                When(number_of_replies=0, then=no_reply),
                When(number_of_replies__gte=1, then=latest_reply)
                )
            )
        queryset = all_posts_list.order_by('-latest_reply', '-created_on')
        return queryset


def view_post(request, slug):
    '''
    Displays a post and all replies
    context: post
    templat: view_post.html
    '''
    post = get_object_or_404(Post.objects, slug=slug)
    return render(
        request,
        'message_board/view_post.html',
        {
            "post": post,
        }
        )


@login_required
def new_post(request):
    '''
    Displays form page to create a post
    '''
    if request.method == 'POST':
        new_post_instance = PostForm(data=request.POST)
        if new_post_instance.is_valid:
            try:
                post = new_post_instance.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, 'New post created')
                return HttpResponseRedirect(reverse('message_board'))
            except ValueError as e:
                pass
    else:
        new_post_instance = PostForm()
    return render(
        request,
        'message_board/new_post.html',
        {
            'new_post': new_post_instance,
        },
    )


@login_required
def edit_post(request, slug):
    '''
    Displays page for edit post form
    '''
    if request.method == 'POST':
        post = get_object_or_404(Post.objects, slug=slug)
        edit_post_form = PostForm(data=request.POST, instance=post)
        if edit_post_form.is_valid:
            try:
                edit_post_instance = edit_post_form.save(commit=False)
                edit_post_instance.author = request.user
                edit_post_instance.save()
                messages.success(request, 'Post updated')
                slug = post.slug
                return HttpResponseRedirect(reverse('view_post', args=[slug]))
            except ValueError as e:
                pass
    else:
        post = get_object_or_404(Post.objects, slug=slug)
        edit_post_form = PostForm(instance=post)
    return render(
        request,
        'message_board/edit_post.html',
        {
            'new_post': edit_post_form,
            'post': post,
        },
    )


@login_required
def new_reply(request, slug):
    '''
    Displays page for new reply form
    '''
    post = get_object_or_404(Post.objects, slug=slug)
    if request.method == 'POST':
        new_reply_instance = ReplyForm(data=request.POST)
        if new_reply_instance.is_valid:
            try:
                reply = new_reply_instance.save(commit=False)
                reply.author = request.user
                reply.original_post = post
                reply.save()
                messages.success(request, 'Reply created')
                return HttpResponseRedirect(reverse('view_post', args=[slug]))
            except ValueError as e:
                pass
    else:
        new_reply_instance = ReplyForm()
    return render(
        request,
        'message_board/new_reply.html',
        {
            'new_reply': new_reply_instance,
            'post': post,
        },
    )


@login_required
def delete_post(request, slug):
    '''
    Deletes post from the database and redirects to message board
    '''
    post = get_object_or_404(Post.objects, slug=slug)
    if request.user == post.author:
        post.delete()
        messages.success(request, 'Post deleted')
    else:
        messages.error(request, 'Permission denied')
    return HttpResponseRedirect(reverse('message_board'))


@login_required
def edit_reply(request, slug, comment_id):
    '''
    Displays page for edit reply form and
    updates database
    '''
    if request.method == 'POST':
        post = get_object_or_404(Post.objects, slug=slug)
        reply = get_object_or_404(Reply.objects, id=comment_id)
        edit_reply_form = ReplyForm(data=request.POST, instance=reply)
        if edit_reply_form.is_valid:
            try:
                edit_reply_instance = edit_reply_form.save(commit=False)
                edit_reply_instance.author = request.user
                edit_reply_instance.save()
                messages.success(request, 'Reply updated')
                slug = post.slug
                return HttpResponseRedirect(reverse('view_post', args=[slug]))
            except ValueError as e:
                pass
    else:
        post = get_object_or_404(Post.objects, slug=slug)
        reply = get_object_or_404(Reply.objects, id=comment_id)
        edit_reply_form = ReplyForm(instance=reply)
    return render(
        request,
        'message_board/edit_reply.html',
        {
            'edit_reply_form': edit_reply_form,
            'post': post,
            'reply': reply,
        },
    )


@login_required
def delete_reply(request, slug, reply_id):
    '''
    Deletes reply from the databse and redirects to the orginal post
    '''
    reply = get_object_or_404(Reply.objects, id=reply_id)
    if request.user == reply.author:
        reply.delete()
        messages.success(request, 'Reply deleted')
    else:
        messages.error(request, 'Permission denied')
    return HttpResponseRedirect(reverse('view_post', args=[slug]))
