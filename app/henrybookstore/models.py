from django.db import models
from tinymce.models import HTMLField
import os
import datetime
from django.core.exceptions import ValidationError


def validate_image_file_extension(value):
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.png','.jpeg','.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def image_upload_location(instance, filename):
    #filebase, extension = filename.split('.')
    extension = os.path.splitext(filename)[1]
    filename = os.path.splitext(filename)[0]
    currentDT = datetime.datetime.now()
    temp = currentDT.strftime("%m%d%H%M%S")
    return 'bookstore_images/%s_%s%s' % (filename, temp, extension)


class Book(models.Model):
    authors = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = HTMLField()
    thumbnail = models.FileField(upload_to=image_upload_location, validators=[validate_image_file_extension])

    def __str__(self):
        return f'{self.authors} - {self.title} {self.price}'
    
class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, through="Inventory")

    def __str__(self):
        return f'{self.name} - {self.address} {self.city}'
    
class Inventory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.book} - {self.branch}: {self.quantity}'