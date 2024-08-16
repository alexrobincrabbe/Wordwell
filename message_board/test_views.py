from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Post, Reply
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
            self.posts.append(Post(author=user, title=f'title-{i}', text="dummy"))
            self.posts[i].save()
            i+=1
        
        #create replies to first post
        self.replies = []
        i=0
        for user in self.users:
            self.replies.append(Reply(author=user, original_post=self.posts[0],text=f"reply-text{i}"))
            self.replies[i].save()
            i+=1
 
    def test_page_message_board(self):
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
        
    def test_post_view(self):
        response = self.client.get(reverse('view_post', args=['title-0']))
        self.assertEqual(response.status_code, 200)

        # Check post fields are displayed
        self.assertIn(b'myUsername0', response.content)
        self.assertIn(b'title-0', response.content)
        self.assertIn(b'dummy', response.content)


        # Check that all replies are displayed on the page
        i=0
        for reply in self.replies:
            self.assertIn(
                bytes(reply.author.username, encoding='utf-8'), response.content
            )
            self.assertIn(
                bytes(reply.text, encoding='utf-8'), response.content
            )
            i+=1