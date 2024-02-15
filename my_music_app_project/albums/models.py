from django.core.validators import MinValueValidator
from django.db import models

from my_music_app_project.profiles.models import Profile

GENRE_CHOICES = [
    ("pop", "Pop Music"),
    ("jazz", "Jazz Music"),
    ("rb", "R&B Music"),
    ("rock", "Rock Music"),
    ("country", "Country Music"),
    ("dance", "Dance Music"),
    ("hiphop", "Hip Hop Music"),
    ("other", "Other"),
]


class Album(models.Model):
    MAX_LENGTH = 30

    album_name = models.CharField(
        max_length=MAX_LENGTH,
        null=False,
        blank=False,
        unique=True,
    )

    artist = models.CharField(
        max_length=MAX_LENGTH,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LENGTH,
        null=False,
        blank=False,
        choices=GENRE_CHOICES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(0.0),]
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="profile_albums",
    )
