from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Views_Test(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        
    def test_get_checkout_page(self):
       
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")