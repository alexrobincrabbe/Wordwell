"""
Instructions app views:
- context: none
- template: index.htm, displays the welcome page with game instructions
"""
from django.shortcuts import render


def instructions(request):
    '''
    Display home page
    '''
    context = {
    }
    return render(request, 'instructions/index.html', context)
