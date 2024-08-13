
from django.test import TestCase
from .forms import ProfileUpdateForm


class TestProfileUpdateForm(TestCase):

    def test_form_is_valid(self):
        """
        Test for non-mandatory fields
        """
        form = ProfileUpdateForm({'display_name':'jack'})
        self.assertTrue(form.is_valid(), msg='Display name was provided, but form is not valid')

    def test_form_is_not_valid(self):
        """
        Test for display_name field
        """
        form = ProfileUpdateForm({'about_me': 'Blah Blah Blah','display_name':''})
        self.assertFalse(form.is_valid(), msg='Display name was not provided, but the form is valid')