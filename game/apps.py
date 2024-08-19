'''
App configurations
'''
from django.apps import AppConfig


class GameConfig(AppConfig):
    '''
    Configiruation for game app
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'game'
