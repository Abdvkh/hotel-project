from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Hotel,\
                    Image,\
                    OpeningHours

class TestPage(TestCase):
    def create_hotel(self, name='Hotel Sayokhat', stars=5, owner="Abubakr Abduvakhidov"):
        return Hotel.objects.create(name=name, stars=stars, owner=owner)

    def create_image(self, path='static/assets/hotel.jpg'):
        image = SimpleUploadedFile(name='hotel.jpg',
                                    content=open(path, 'rb').read(),
                                    content_type='image/jpeg')

        return Image.objects.create(image=image)

    def create_open_hours(self, weekday=1, from_hour=timezone.now(), to_hour=timezone.now()):
        return OpeningHours.objects.create(weekday=weekday,
                                           from_hour=from_hour,
                                           to_hour=to_hour)

    def test_no_hotel_in_db_but_image_and_hours(self):
        img = self.create_image()
        open_hours = self.create_open_hours()

        response = self.client.get(reverse('home'))

        self.assertTrue(isinstance(img, Image))
        self.assertTrue(isinstance(open_hours, OpeningHours))

        self.assertEqual(response.status_code, 404)

    def test_no_images_in_db_but_hotel_and_hours(self):
        hotel = self.create_hotel()
        open_hours = self.create_open_hours()

        response = self.client.get(reverse('home'))

        self.assertTrue(isinstance(hotel, Hotel))
        self.assertTrue(isinstance(open_hours, OpeningHours))

        self.assertEqual(response.status_code, 404)

    def test_no_hours_in_db_but_hotel_and_image(self):
        hotel = self.create_hotel()
        img = self.create_image()

        response = self.client.get(reverse('home'))

        self.assertTrue(isinstance(img, Image))
        self.assertTrue(isinstance(hotel, Hotel))

        self.assertEqual(response.status_code, 200)

    def test_home(self):
        self.create_hotel()
        self.create_open_hours()
        self.create_image()

        response = self.client.get(reverse('home'))

        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, str(timezone.now().hour)+':'+str(timezone.now().minute))
