from django.db import models

# Create your models here.
class Shoes(models.Model):
    name=models.CharField(max_length=255)
    brand=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    date=models.DateTimeField()
    display_image=models.ImageField(upload_to='images/')
    image1=models.ImageField(upload_to='images/')
    image2=models.ImageField(upload_to='images/')
    image3=models.ImageField(upload_to='images/')
    

    def __str__(self):
        return self.name