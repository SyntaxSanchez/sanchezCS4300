from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('booking_history/', views.booking_history, name='booking_history'),
    path('book_seat/<int:movie_id>/', views.book_seat, name='book_seat'),
]
