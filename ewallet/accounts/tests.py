from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class UserAuthTests(TestCase):
    def setUp(self):
        """Créer un utilisateur de test"""
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_signup(self):
        """Test de l'inscription"""
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirection après inscription
        self.assertTrue(User.objects.filter(username='newuser').exists())  # Vérifie que l'utilisateur est bien créé

    def test_login(self):
        """Test de la connexion"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirection après connexion
        self.assertTrue('_auth_user_id' in self.client.session)  # Vérifie que l'utilisateur est connecté

    def test_logout(self):
        """Test de la déconnexion"""
        self.client.login(username='testuser', password='testpassword')  # Connexion
        response = self.client.get(reverse('logout'))  # Déconnexion
        self.assertEqual(response.status_code, 302)  # Redirection après déconnexion
        self.assertFalse('_auth_user_id' in self.client.session)  # Vérifie que l'utilisateur est déconnecté

class FrontendTests(TestCase):
    def test_signup_page_loads(self):
        """Test si la page d'inscription charge correctement"""
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_login_page_loads(self):
        """Test si la page de connexion charge correctement"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
