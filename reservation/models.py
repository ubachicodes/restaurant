from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.PositiveIntegerField(default="2")

    def __str__(self):
        return f"Table {self.number} (Capacity: {self.capacity})"

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    num_persons = models.PositiveIntegerField(default="2")
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time} (Table: {self.table.number})"
