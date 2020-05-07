from django.test import TestCase
from catalog.models import *
import pytest

class ModelTest(TestCase):

    def test_PartOfTheWorld(self):
        partoftheworld = PartOfTheWorld.objects.create()
        partoftheworld.name = 'Европа'
        assert partoftheworld.__str__() == 'Европа'

    def test_Cities(self):
        cities = Cities.objects.create()
        cities.name = 'Минск'
        cities.save()
        assert cities.__str__() == 'Минск'

    def test_Tags(self):
        tags = Tags.objects.create()
        tags.name = 'Родина'
        tags.save()
        assert tags.__str__() == 'Родина'

    def test_Places(self):
        partoftheworld = PartOfTheWorld.objects.create(name='Европа')
        country = Countries.objects.create(name='Франция')
        city = Cities.objects.create(name='Франция')
        places = Places.objects.create(part_of_the_world=partoftheworld, country=country, city=city, name='Эйфелевая башня', description='Описание', image='media/2-Zhangye_Danxia_Landform-e1528945590663.jpg')
        assert places.__str__() == 'Эйфелевая башня'


@pytest.mark.parametrize("countries_name", ['Беларусь', 'Россия'])
def test_Countries(countries_name):
    countries = Countries.objects.create()
    countries.name = countries_name
    countries.save()
    assert countries.__str__() == countries_name