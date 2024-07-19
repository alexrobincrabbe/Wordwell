from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def instructions(request):
    '''
    Display home page
    '''
    context = {
    }
    return render(request, 'instructions/index.html',context)