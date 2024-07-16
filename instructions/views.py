from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Instructions(request):
    '''
    Display home page
    '''
    return HttpResponse(render(request, 'instructions/index.html'))