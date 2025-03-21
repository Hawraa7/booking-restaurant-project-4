from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    
    def __str__(self):
        return f"Table {self.number} - {self.capacity} seats"
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    # Prevent double bookings
    class Meta:
        unique_together = ('table', 'date', 'time')  
    
    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"
    
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    
    def __str__(self):
        return self.name