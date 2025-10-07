
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from bookings.models import Movie, Seat, Booking
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.utils import timezone
from django.db import transaction

# REST API ViewSets
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    @action(detail=False, methods=['get'])
    def available(self, request):
        available_seats = Seat.objects.filter(is_booked=False)
        serializer = self.get_serializer(available_seats, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def booked(self, request):
        booked_seats = Seat.objects.filter(is_booked=True)
        serializer = self.get_serializer(booked_seats, many=True)
        return Response(serializer.data)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all() 
    serializer_class = BookingSerializer

    def get_queryset(self):
        # Return all bookings (no user filtering)
        return Booking.objects.all()

    def perform_create(self, serializer):
        with transaction.atomic():
            seat = serializer.validated_data['seat']
            if seat.is_booked:
                raise serializers.ValidationError("Seat already booked.")
            seat.is_booked = True
            seat.save()
            serializer.save()

# Django Template Views
def movie_list(request):
    # List all the movies that are gonna be on the frontent
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def book_seat(request, movie_id):
    # Book the seat for the movie
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all().order_by('seat_number')

    if request.method == "POST":
        seat_id = request.POST.get("seat")
        seat = get_object_or_404(Seat, id=seat_id)

        if seat.is_booked:
            error = "This seat is already booked."
            return render(request, 'bookings/seat_booking.html', {
                'movie': movie,
                'seats': seats,
                'error': error
            })

        seat.is_booked = True
        seat.save()

        Booking.objects.create(movie=movie, seat=seat, booking_date=timezone.now())
        return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': seats
    })

def booking_history(request):
    """Show booking history (all bookings)"""
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
