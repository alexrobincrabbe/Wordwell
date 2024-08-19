'''
App config
'''

from django.apps import AppConfig


class HighscoresConfig(AppConfig):
    '''
    configure highscores app
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'highscores'
