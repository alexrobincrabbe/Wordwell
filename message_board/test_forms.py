'''
message_board app form tests
'''
from django.test import TestCase
from .forms import PostForm, ReplyForm


class TestProfileUpdateForm(TestCase):
    '''
    Test all forms
    '''
    def test_post_form_is_valid(self):
        """
        Test is valid with mandatory fields name completed
        """
        form = PostForm({'title': 'testTitle', 'text': 'testText'})
        self.assertTrue(
            form.is_valid(),
            msg='Mandatory fields were provided, but form is not valid'
            )

    def test_post_form_is_not_valid(self):
        """
        Test is not valid without mandatory fields
        """
        form = PostForm({'title': '', 'text': 'testText'})
        self.assertFalse(form.is_valid(),
                         msg='Title was not provided, but the form is valid')
        form = PostForm({'title': 'textTitle', 'text': ''})
        self.assertFalse(form.is_valid(),
                         msg='Text was not provided, but the form is valid')

    def test_reply_form_is_valid(self):
        """
        Test is valid with mandatory fields name completed
        """
        form = ReplyForm({'text': 'testText'})
        self.assertTrue(
            form.is_valid(),
            msg='Mandatory fields were provided, but form is not valid'
            )

    def test_reply_form_is_not_valid(self):
        """
        Test is not valid without mandatory fields
        """
        form = ReplyForm({'text': ''})
        self.assertFalse(form.is_valid(),
                         msg='Text was not provided, but the form is valid')
