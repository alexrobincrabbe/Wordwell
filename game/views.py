"""
Game app views
"""
import json
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from profile_page.models import UserProfile
from wordwell.settings import BASE_DIR
from .models import Scores

# Create your views here.
@csrf_exempt
def game(request):
    """
    View to:
    - Display the game page
    - Save the score to the database
    """
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
    """
    Upload the dictionary to the dictionary url, so that is can
    be retreived at the front end by the fetch api
    """
    dictionary_path="game/static/game/dictionary.json"
    file_path = os.path.join(BASE_DIR, dictionary_path)
    with open(file_path, 'r', encoding="utf-8") as f:
        json_dictionary = json.load(f)
    return JsonResponse(json_dictionary)
