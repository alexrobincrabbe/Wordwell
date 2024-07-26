from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def game(request):
    return render(
        request,
        "game/game.html",
    )

def dictionary(request):
    f = open('/workspace/Wordwell/static/dictionary/dictionary.json')  
    dictionary = json.load(f)
    return JsonResponse(dictionary)
