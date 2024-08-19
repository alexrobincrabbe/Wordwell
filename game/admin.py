'''
Register models in admin site
'''
from django.contrib import admin
from .models import Scores

# Register your models here.

admin.site.register(Scores)
