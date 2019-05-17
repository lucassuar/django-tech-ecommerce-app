from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class TestViews(TestCase):
        
    def test_get_registerPage(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
        
    def test_get_profilePage(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
        
    def test_get_loginPage(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        
