from django.http import HttpRequest
from django.test import TestCase, Client
from django.urls import resolve
from lists.views import home_page
from lists.models import Item


# Create your tests here.
# class smokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1 + 2, 3)


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        res2 = self.client.get('/')
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
        self.assertTemplateUsed(res2, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())




class ItemModelTest(TestCase):
    def test_saving_and_retrieving_item(self):
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()
        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
