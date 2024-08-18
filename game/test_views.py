from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User
from .models import Scores
# Create your tests here.


class testGameViews(TestCase):

    def setUp(self):
        """
        Create a user and complete profile for user
        """
        #create user
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
        )
    

    def test_game_view(self):
        # user must be logged in to save score
        self.client.login(
            username="myUsername", password ="myPassword")
        
        response=self.client.get(reverse('game'))
        self.assertEqual(response.status_code, 200)

        post_data = {
            'score': 3142,
        }
        # check score does not exist in database
        score = Scores.objects.filter(score=3142).exists()
        self.assertEqual(score, False)
        # check score exists after score is sent as post request
        post_response = self.client.post(reverse('game'), post_data)
        self.assertEqual(post_response.status_code, 200)
        score = Scores.objects.filter(score=3142).exists()
        self.assertEqual(score, True)


