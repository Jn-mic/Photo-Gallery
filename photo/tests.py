from django.test import TestCase
from .models import Location, Category,Image


def test_delete_image(self):
    '''
    Test the deletion of an instance
    '''
    self.image.save_image()
    self.image.delete_image()
    self.assertTrue(len(Image) == 0)

def test_get_image_by_id(self):
    self.image.save_image()
    image_id= self.image.pk
    image_by_id = Image.get_image_by_id(image_id)
    self.assertEqual(self.image,image_by_id)

def test_search_image(self):
    self.image.save_image()
    name = self.image.image_name
    found_image = Image.search_image(name)
    self.assertTrue(len(found_image) == 1)

def test_filter_by_location(self):
    self.image.save_image()
    location = self.image.location
    found_images = Image.filter_by_location(location)
    self.assertEqual(self.image,found_images)

def tearDown(self):
    Image.objects.all().delete()
    Location.objects.all().delete()
    Category.objects.all().delete()