from django.shortcuts import render
from django.http import JsonResponse
import json
import os
from wordwell.settings import BASE_DIR
from .models import Scores
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from profile_page.models import UserProfile

# Create your views here.
@csrf_exempt
def game(request):
    if request.method == 'POST':
        score = request.POST['score']
        score = int(score)
        new_score = Scores(profile=request.user.profile, score=score)
        new_score.save()
        high_score = request.user.profile.high_score
        profile = UserProfile.objects.get(user=request.user)
        if score > high_score:
            profile.high_score = score
            profile.save()

    return render(
        request,
        "game/game.html",
    )

def dictionary(request):
    dictionary_path="game/static/game/dictionary.json"
    file_path = os.path.join(BASE_DIR, dictionary_path)
    f = open(file_path)  
    dictionary = json.load(f)
    return JsonResponse(dictionary)
