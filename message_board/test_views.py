from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Post
import random

class TestHighscoreViews(TestCase):
    '''
    Tests that:
    page returns status of 200 when high score page is displayed
    Checks all usernames and highscores are returned in the html
    
    '''
    
    def setUp(self):
        """
        Create users and a post for each user
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
        #create posts
        self.posts =[]
        i=0
        for user in self.users:
            self.posts.append(Post(author=user, title=f'title-{i}', text="dummy", slug=f"title{i}"))
            self.posts[i].save()
            i+=1

    def test_page_contains_usernames_and_tiles(self):
        '''
        Tests that all usernames and post titles in the database are displayed in the returned html
        
        '''
        response = self.client.get(reverse('message_board'))
        self.assertEqual(response.status_code, 200)

        # Check that usernames and titles are all displayed on the page
        i=0
        for user in self.users:
            self.assertIn(
                bytes(user.username, encoding='utf-8'), response.content
            )
            self.assertIn(
                bytes(self.posts[i].title, encoding='utf-8'), response.content
            )
            i+=1
