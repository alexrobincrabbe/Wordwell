from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Post, Reply

class TestMessageBoardViews(TestCase):
    '''
    Tests all message board views
    
    '''
    
    def setUp(self):
        """
        Create users and a post for each user
        create replies for first post
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
        Tests that all usernames and post titles in the database are displayed on the page
        
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
        '''
        check that the correct username, title, and text are displayed on the view post page
        checks that the text and authors of all replies are displayed on the view post page
        '''
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

    def test_new_post_view_is_valid(self):
        '''
        Check that the response is redirected(status 302)
        Check that the redirect returns a response status of 200
        Check that the success message is displayed if the form is valid
        '''

        self.client.login(
            username="myUsername1", password ="myPassword1")
        post_data = {
            'title':'thisTitle',
            'text':'thisText',
        }
        response = self.client.post(reverse('new_post'), post_data)
        redirect_response = self.client.post(reverse('new_post'), post_data, follow=True)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(redirect_response.status_code, 200)
        self.assertIn(
            b'New post created', redirect_response.content, msg="Form was valid but success message was not displayed"
        )

    def test_new_post_view_is_invalid(self):
        '''
        Check that the response is not redirected and returns a status of 200
        if mandatory fields are not complete
    
        '''
        self.client.login(
            username="myUsername1", password ="myPassword1")
        # Without Title
        post_data = {
            'title':'',
            'text':'thisText',
        }

        response = self.client.post(reverse('new_post'), post_data)        
        self.assertEqual(response.status_code, 200)

        # Without text
        post_data = {
            'title':'thisTitle',
            'text':'',
        }

        response = self.client.post(reverse('new_post'), post_data)        
        self.assertEqual(response.status_code, 200)

    def test_edit_post_view(self):
        '''
        check that the edit post page returns a status of 200 for a get request
        check that the content is hidden if the user is not the author of the post
        check that the form is prepoluated with the post title and content
        '''
        self.client.login(
        username="myUsername1", password ="myPassword1")
        # get post that is authored by logged in user
        get_response=self.client.get(reverse('edit_post', args=['title-1']))
        self.assertEqual(get_response.status_code, 200)
        self.assertNotIn(b'you do not have permission to view this page', get_response.content)
        # Form is prepoluated with the post fields
        self.assertIn(bytes(self.posts[1].title, encoding='utf-8'), get_response.content)
        self.assertIn(bytes(self.posts[1].text, encoding='utf-8'), get_response.content)
        # page content is not shown if the logged in user is not the post author
        get_response_forbidden=self.client.get(reverse('edit_post', args=['title-2']))
        self.assertEqual(get_response_forbidden.status_code, 200)
        self.assertIn(b'you do not have permission to view this page', get_response_forbidden.content)
    
    def test_edit_post_form_is_valid(self):
        '''
        check that the page redirects and a success message is shown when the form is valid
        '''
        self.client.login(
        username="myUsername1", password ="myPassword1")
        # Check that the page is redirected, and shows the success message when the form is valid
        post_data = {
            'title':'newTitle',
            'text':'thisText',
        }
        post_response = self.client.post(reverse('edit_post',args=['title-1']), post_data)
        post_response_redirect = self.client.post(reverse('edit_post',args=['newtitle']), post_data, follow=True)
        self.assertEqual(post_response.status_code, 302)
        self.assertEqual(post_response_redirect.status_code, 200)
        self.assertIn(b'Post updated',post_response_redirect.content)

    def test_edit_post_form_is_not_valid(self):
        '''
        check that the page does not redirect if the form is invalid
        '''
        self.client.login(
        username="myUsername1", password ="myPassword1")
        invalid_post_data = []
        # no title
        invalid_post_data.append({
            'title':'',
            'text':'thisText',
        })
        # no text
        invalid_post_data.append({
            'title':'newTitle',
            'text':'',
        })
        # duplicate title
        invalid_post_data.append( {
            'title':'title-2',
            'text':'newText',
        })
        for post_data in invalid_post_data:
            post_response = self.client.post(reverse('edit_post',args=['title-1']), post_data)
            self.assertEqual(post_response.status_code, 200)