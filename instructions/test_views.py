from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.


class testInstructionsViews(TestCase):

    def test_instructions_view(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)