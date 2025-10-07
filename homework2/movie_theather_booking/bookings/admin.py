from django.contrib import admin
from .models import Movie, Seat, Booking

# Register your models so they show up in the admin panel
admin.site.register(Movie)
admin.site.register(Seat)
admin.site.register(Booking)
