from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Meals(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    calories = models.IntegerField()
    price =  models.DecimalField(max_digits=5 , decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='meals/')
    is_vegetarian = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    slug = models.SlugField(blank=True , null=True)

    def save (self, *args, **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Meals, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def _str_(self):
        return self.name