import pytest
from django.test import TestCase, Client
from catalog.models import *
from django.urls import reverse


class AuthorListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_places = 13
        for places_num in range(number_of_places):
            Places.objects.create(name=places_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/places/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('places'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('places'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/places_list.html')


@pytest.fixture
def test_user(db):
    user = CustomUser.objects.create_user(username='Nik', email='nik@gmail.com', password='1a2b3c4d5d1337')
    user.save()
    return user


def test_home():
    c = Client()
    c.login(username='Nik', password='1a2b3c4d5d1337')
    response = c.post('/catalog/')
    assert response.status_code == 200
