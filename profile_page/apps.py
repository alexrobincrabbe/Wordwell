'''
App configs
'''
from django.apps import AppConfig


class ProfilePageConfig(AppConfig):
    '''
    profile_page app config
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile_page'

    def ready(self):
        '''
        import signal to create user profile when a user is created
        '''
        import profile_page.signals
