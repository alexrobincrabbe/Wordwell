'''
App configs
'''
from django.apps import AppConfig


class MessageBoardConfig(AppConfig):
    '''
    MessageBoard config
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'message_board'
