'''
Instructions app views tests
'''

from django.test import TestCase
from django.shortcuts import reverse


class TestInstructionsViews(TestCase):
    '''
    tests:
    - test_instructions_view
    '''
    def test_instructions_view(self):
        '''
        Checks that the page laods
        '''
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
