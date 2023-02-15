from django.test import TestCase
from mixer.backend.django import mixer
from .models import Link, Firma, Zarplata, Region, Position


class LinkTestMixer(TestCase):
    def setUp(self):
        self.link = mixer.blend(Link)
        self.firma = mixer.blend(Firma)
        self.zarplata = mixer.blend(Zarplata)
        self.region = mixer.blend(Region)
        self.position = mixer.blend(Position)

    def test_Firma(self):
        self.assertIsNotNone(self.firma)

    def test_Zarplata(self):
        self.assertIsNotNone(self.zarplata)

    def test_Region(self):
        self.assertIsNotNone(self.region)

    def test_Position(self):
        self.assertIsNotNone(self.position)

# Create your tests here.
