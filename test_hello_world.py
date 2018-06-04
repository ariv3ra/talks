import hello_world
import unittest

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.app = hello_world.app.test_client()
        self.app.testing = True
    def test_default_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    def test_hello_message(self):
        response = self.app.get('/')
        message = 'Hello DockerCon 2018!'
        self.assertEqual(response.data, hello_world.wrap_html(message))

if __name__ == '__main__':
    unittest.main()