from flask_testing import TestCase
from flask import current_app, url_for

from main import app



class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app
#Metodo para probar que app existe
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

#Metodo para probar que la app esta en modo de test
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

#Probar que la redireccion de index a hello se cumple
    def test_index_redirects(self):
        response = self.client.get(url_for('index'))

        self.assertRedirects(response, url_for('hello'))

#Probar que la peticion a la tuta hello retorne 200
    def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response)

    def test_hello_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake-pass'
        }
        response = self.client.post(url_for('hello'), data=fake_form)
        self.assertRedirects(response, url_for('index'))

    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)
