from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveIntegerField()

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.number} (Capacity: {self.capacity})"