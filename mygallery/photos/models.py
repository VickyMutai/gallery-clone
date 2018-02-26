from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name    

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(upload_to = 'categories/',null=True,blank=True)
    location = models.ManyToManyField(Location)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['upload_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def filter_by_location(cls,id):
        images = Image.objects.filter(id=location.id)
        return images

    @classmethod
    def search_by_category(cls, search_term):
        category = cls.objects.filter(category__category_name__icontains=search_term)
        return category 