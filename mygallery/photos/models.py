from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name    

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
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