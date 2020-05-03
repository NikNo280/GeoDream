from django.test import TestCase

from catalog.models import Places, PartOfTheWorld, Countries, Cities, Tags

class PlacesModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Places.objects.create(part_of_the_world=PartOfTheWorld.objects.create(name='Европа'),
                              country=Countries.objects.create(name='Беларусь'),
                              city=Cities.objects.create(name='Минск'),
                              name='Музей ВОВ', description='Описание музея')

    def test_places_part_of_the_world(self):
        places = Places.objects.get(id=1)
        places_part_of_the_world = places._meta.get_field('part_of_the_world').verbose_name
        self.assertEquals(places_part_of_the_world, 'part of the world')

    def test_places_country(self):
        places = Places.objects.get(id=1)
        places_part_of_the_world = places._meta.get_field('country').verbose_name
        self.assertEquals(places_part_of_the_world, 'country')

    def test_places_city(self):
        places = Places.objects.get(id=1)
        places_part_of_the_world = places._meta.get_field('city').verbose_name
        self.assertEquals(places_part_of_the_world, 'city')

    def test_places_name(self):
        places = Places.objects.get(id=1)
        places_name = places._meta.get_field('name').verbose_name
        self.assertEquals(places_name, 'name')

    def test_places_description(self):
        places = Places.objects.get(id=1)
        places_description = places._meta.get_field('description').verbose_name
        self.assertEquals(places_description, 'description')

    def test_object_name(self):
        places = Places.objects.get(id=1)
        expected_object_name = '%s' % (places.name)
        self.assertEquals(expected_object_name, str(places))

    def test_get_absolute_url(self):
        places = Places.objects.get(id=1)
        self.assertEquals(places.get_absolute_url(), '/catalog/places/1')