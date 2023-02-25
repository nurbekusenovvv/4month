from django.test import TestCase , Client
from django.urls import reverse

class MyTestDjango(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hibro(self):
        response = self.client.get(reverse("hello-view"))
        expected_data = "<h1>Hello<h1>"
        expected_header = "Alex"

        self.assertEqual(response.content.decode(), expected_data)
        self.assertEqual(response.status_code, 300)
        self.assertEqual(response.headers["names"], expected_header)
    
    def test_get_inf(self):
        response_get = self.client.get(reverse("index-page"))
        response_post = self.client.post(reverse("index-page"))

        expected_get = "Главная страница"
        expected_post = "Не тот метод запроса"

        self.assertEqual(response_get.status_code ,200)
        self.assertEqual(response_post.status_code , 200)
        self.assertEqual(response_get.content.decode(), expected_get)
        self.assertEqual(response_post.content.decode(), expected_post)

    def test_get_con(self):
        response_get_contact = self.client.get(reverse("endpoint-contact"))

        expect_contact = "contacts"

        self.assertEqual(response_get_contact.content.decode(),expect_contact)
        self.assertEqual(response_get_contact.status_code,200)
        
    def test_get_abt(self):
        response_get_about = self.client.get(reverse("get-about"))

        expected_about = "about"

        self.assertEqual(response_get_about.content.decode(), expected_about)
        self.assertEqual(response_get_about.status_code,200)