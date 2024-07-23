from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post

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
