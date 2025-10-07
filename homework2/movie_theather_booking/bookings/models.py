from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='seats')  
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Seat {self.seat_number} for {self.movie.title}"


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.seat} booked for {self.movie}"


    def __str__(self):
        return f"{self.user.username} booked {self.seat} for {self.movie}"
