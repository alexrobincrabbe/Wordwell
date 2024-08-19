''''
High score app views:
- high_scores
'''
from django.shortcuts import render
from django.contrib.auth.models import User


def high_scores(request):
    '''
    template: highscores.html - page displaying high scores of all users
    context: user_list - list of all users
    '''
    user_list = User.objects.all().order_by('-profile__high_score')

    return render(
        request,
        "highscores/highscores.html",
        {
            "user_list": user_list
        },
    )
