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

    def test_save_category(self):
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_category(self):
        self.nature.save_category()
        self.nature.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)<1)


class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        self.tsavo = Location(name="Tsavo")

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.tsavo,Location))

    def test_save_location(self):
        self.tsavo.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_location(self):
        self.tsavo.save_location()
        self.tsavo.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)<1)

class ImageTestClass(TestCase):
    #set up method
    def setUp(self):
        self.elephant = Image(name="Elephant",description="It is super big")
        self.elephant.save()

        #creating new category and saving it
        self.nature = Category(name="nature")
        self.nature.save()

        #creating new location and saving it
        self.tsavo = Location(name="Tsavo")
        self.tsavo.save()

        self.elephant.location.add(self.tsavo)
        self.elephant.category.add(self.nature)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

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

