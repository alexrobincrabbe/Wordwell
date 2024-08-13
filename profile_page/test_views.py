from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import UserProfile
import datetime

class TestProfilePageViews(TestCase):
    
    def setUp(self):
        """
        Create a user and complete profile for user
        """
        #create user
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        #get profile and fill in fields
        self.profile=UserProfile.objects.filter(user=self.user)
        self.profile.update(
            about_me="blah blah blah",
            high_score=123456,
            display_name="Bucky",
            )
        self.profile[0].save()

    def test_update_profile(self):
        self.client.login(
            username="myUsername", password ="myPassword")
        post_data = {
            'email':'myEmail',
            'display_name':'myDisplayName',
            'about_me':'aboutMeText',
        }
        response = self.client.post(reverse('update_profile'), post_data)
        self.assertEqual(response.status_code, 200)
        #self.assertIn(
        #    b'Your account has been updated', response.content
        #)

    def test_view_profile(self):
        """
        Test the view profile page
        Check that page exists
        Check that user and user profile info is displayed on the page
        """
        join_date=self.user.date_joined.strftime("%b. %d, %Y, %-I:%M")
        
        response = self.client.get(reverse('view_profile', args=['myusername']))
        self.assertEqual(response.status_code, 200) #url exists
        self.assertIn(b"blah blah blah", response.content) #about_me
        self.assertIn(b"123456", response.content) #high_score
        self.assertIn(b"Bucky", response.content) #display_name
        self.assertIn(bytes(join_date,encoding='utf-8'), response.content)