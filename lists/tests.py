from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # we request the specified template
        request = HttpRequest()
        response = home_page(request)
        # the returned html should match the template
        # render_to_string does exactly what it says on the tin
        expected_html = render_to_string('home.html')
        # response is returned as raw bytes thus gets decoded
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_process_post_request(self):
        request = HttpRequest()
        request.method = 'POST'
        # use POST to send string to 'item_text'
        # POST data is sent as name-value pair
        request.POST['item_text'] = 'A new list item'

        # request page with POST with specified values, store in response
        response = home_page(request)

        # check if expected value appears in response
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new list item'}
        )
        # check if resulting html is just as we want
        self.assertEqual(response.content.decode(), expected_html)

# Create your tests here.
