from django.shortcuts import render
from django.http import JsonResponse
import json
import os
from wordwell.settings import BASE_DIR

# Create your views here.

def game(request):
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
