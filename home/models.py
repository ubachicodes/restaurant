from django.db import models

# Create your models here.

class HomePage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='home_images/')

    def __str__(self):
        return self.title