from django.test import TestCase
from .forms import ProfileUpdateForm, UserUpdateForm


class TestProfileUpdateForm(TestCase):

    def test_profile_form_is_valid(self):
        """
        Test is valid with mandatory field display name completed
        """
        form = ProfileUpdateForm({'display_name':'jack'})
        self.assertTrue(form.is_valid(), msg='Display name was provided, but form is not valid')


    def test_profile_form_is_not_valid(self):
        """
        Test is not valid without display_name field
        """
        form = ProfileUpdateForm({'about_me': 'Blah Blah Blah','display_name':''})
        self.assertFalse(form.is_valid(), msg='Display name was not provided, but the form is valid')

    def test_user_form_is_valid_without_email(self):
        """
        Test is valid with no email
        """
        form = UserUpdateForm({'email':''})
        self.assertTrue(form.is_valid(), msg='Email was blank, but form is not valid')

    def test_user_form_is_valid_with_email(self):
        """
        Test is valid with valid email
        """
        form = UserUpdateForm({'email':'jack@gmail.com'})
        self.assertTrue(form.is_valid(), msg='Email was valid, but form is not valid')

    def test_user_form_is_not_valid(self):
        """
        Test is not valid with invalid email
        """
        form = UserUpdateForm({'email': 'invadidEmail'})
        self.assertFalse(form.is_valid(), msg='Email was invalid, but the form is valid')