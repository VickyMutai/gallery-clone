from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.

class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        self.nature = Category(name="nature")

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Category))

class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        self.tsavo = Location(name="Tsavo")

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.tsavo,Location))

class ImageTestClass(TestCase):
    #set up method
    def setUp(self):
        self.elephant = Image(name="Elephant",description="It is super big")

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.elephant,Image))

    def test_save_image(self):
        self.elephant.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.elephant.save_image()
        self.elephant.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)<1)

