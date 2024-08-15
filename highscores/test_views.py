from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from profile_page.models import UserProfile
import random

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
        #create users
        self.users =[]
        for i in range(0,10):
            self.users.append(User.objects.create_superuser(
            username=f"myUsername{i}",
            password=f"myPassword{i}",
            email=f"test{i}@test.com"
            )
        )
        #get profiles and fill in high scores
        self.profiles =[]
        i=0
        for user in self.users:
            self.profiles.append(UserProfile.objects.filter(user=user))
            self.profiles[i].update(
                high_score=random.randrange(1,1000),
            )
            self.profiles[i][0].save()
            i+=1

    def test_page_contains_usernames_and_highscores(self):
        '''
        Tests that all usernames and highscores in the database are displayed in the returned html
        Checks that the context data returned is a query set of users ordered by high score
        
        '''
        response = self.client.get(reverse('highscores'))
        self.assertEqual(response.status_code, 200)

        # Check that the correct context is sent with the correct ordering from the view
        context_data =list(response.context[0]['user_list'].all())
        ordered_user_list = list(User.objects.all().order_by('-profile__high_score'))
        self.assertEqual(context_data, ordered_user_list)

        # Check that usernames and highscores are all displayed on the page
        for user in self.users:
            self.assertIn(
                bytes(user.username, encoding='utf-8'), response.content
            )
            self.assertIn(
                bytes(str(user.profile.high_score), encoding='utf-8'), response.content
            )
