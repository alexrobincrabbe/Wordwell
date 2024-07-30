from django.shortcuts import render
from django.http import JsonResponse
import json
import os
from wordwell.settings import BASE_DIR
from .models import Scores
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def game(request):
    if request.method == 'POST':
        score=request.POST['score']
        new_score = Scores(player=request.user, score=score)
        new_score.save()
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
