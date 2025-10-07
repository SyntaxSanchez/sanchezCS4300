from django.test import TestCase
from .models import Movie
from datetime import date

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie1 = Movie.objects.create(
            title="The Fantastic Four: First Steps",
            description="Set against the vibrant backdrop of a 1960s-inspired, retro-futuristic world...",
            release_date=date.today(),
            duration=125 
        )
        self.movie2 = Movie.objects.create(
            title="Star Wars: The Rise of Skywalker",
            description="When it's discovered that the evil Emperor Palpatine did not die...",
            release_date=date.today(),
            duration=142
        )
        self.movie3 = Movie.objects.create(
            title="Superman",
            description="When Superman gets drawn into conflicts at home and abroad...",
            release_date=date.today(),
            duration=129
        )
        self.movie4 = Movie.objects.create(
            title="Avatar: The Way of Water",
            description="Jake Sully and Ney'tiri have formed a family...",
            release_date=date.today(),
            duration=192 
        )
        self.movie5 = Movie.objects.create(
            title="Baby Driver",
            description="Baby is a young and partially hearing impaired getaway driver...",
            release_date=date.today(),
            duration=113
        )
        self.movie6 = Movie.objects.create(
            title="Tron: Ares",
            description="Mankind encounters AI beings for the first time...",
            release_date=date.today(),
            duration=119
        )

    def test_movie_count(self):
        self.assertEqual(Movie.objects.count(), 6)

    def test_movie1_title(self):
        self.assertEqual(self.movie1.title, "The Fantastic Four: First Steps")

    def test_movie2_duration(self):
        self.assertEqual(self.movie2.duration, 142)

    def test_movie4_title(self):
        self.assertEqual(self.movie4.title, "Avatar: The Way of Water")

    def test_movie5_str_output(self):
        self.assertEqual(str(self.movie5), "Baby Driver")
