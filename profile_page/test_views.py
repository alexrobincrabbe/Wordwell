from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import UserProfile

class TestProfilePageViews(TestCase):
    '''
    Tests that:
    page returns status of 200 and success message when profile is updated
    page does not display success message if the form is not valid on submission
    View profile page contains all of the correct profile information
    
    '''
    
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

    def test_update_profile_with_display_name_success(self):
        '''
        check that the view returns a status of 200
        check that the view shows the success message if the form is valid
        '''
        #user must be logged in to update profile
        self.client.login(
            username="myUsername", password ="myPassword")
        #email is blank and display name is completed
        post_data = {
            'email':'',
            'display_name':'myDisplayName',
            'about_me':'',
        }
        response = self.client.post(reverse('update_profile'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Your account has been updated', response.content, msg="Form was valid but success message was not displayed"
        )

    def test_update_profile_with_valid_email(self):
        '''
        check that the view returns a status of 200
        check that the view shows the success message if the form is valid
        '''
        #user must be logged in to update profile
        self.client.login(
            username="myUsername", password ="myPassword")
        #email is valid and display name is completed
        post_data = {
            'email':'jack@email.com',
            'display_name':'myDisplayName',
            'about_me':'',
        }
        response = self.client.post(reverse('update_profile'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Your account has been updated', response.content, msg="Form was valid but success message was not displayed"
        )

    def test_update_profile_without_display_name(self):
        '''
        check that the view returns a status of 200
        check that the view does not show the success message if the form is not valid
        '''
        #user must be logged in to update profile
        self.client.login(
            username="myUsername", password ="myPassword")
        #Display name is blank
        post_data = {
            'email':'email@gmail.com',
            'display_name':'',
            'about_me':'aboutMeText',
        }
        response = self.client.post(reverse('update_profile'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(
            b'Your account has been updated', response.content, msg="Display name was left empty but success message was displayed"
        )

    def test_update_profile_with_invalid_email(self):
        '''
        check that the view returns a status of 200
        check that the view does not show the success message if the form is not valid
        '''
        #user must be logged in to update profile
        self.client.login(
            username="myUsername", password ="myPassword")
        #Email is invalid
        post_data = {
            'email':'invalidemail',
            'display_name':'Jack',
            'about_me':'aboutMeText',
        }
        response = self.client.post(reverse('update_profile'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(
            b'Your account has been updated', response.content, msg="Email was invalid but success message was displayed"
        )

    def test_view_profile(self):
        """
        Test the view profile page
        Check that page exists
        Check that user and user profile info is displayed on the page
        """
        #set login date equal to joined date
        self.user.last_login=self.user.date_joined
        #format dates as shown on the page
        join_date=self.user.date_joined.strftime("%b. %d, %Y, %-I:%M")
        last_login=self.user.last_login.strftime("%b. %d, %Y, %-I:%M")

        response = self.client.get(reverse('view_profile', args=['myusername']))
        self.assertEqual(response.status_code, 200) #url exists and loads page
        self.assertIn(b"blah blah blah", response.content, msg="About me was not displayed on profile") #about_me
        self.assertIn(b"123456", response.content,  msg="High score was not displayed on profile") #high_score
        self.assertIn(b"Bucky", response.content, msg="Display name was not displayed on profile") #display_name
        self.assertIn(bytes(join_date,encoding='utf-8'), response.content, msg="Join date was not displayed on profile") #join date
        self.assertIn(bytes(last_login,encoding='utf-8'), response.content, msg="Last login was not displayed on profile") #login date