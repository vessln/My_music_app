from django.core.validators import MinValueValidator
from django.db import models

from my_music_app_project.profiles.models import Profile

GENRE_CHOICES = [
    ("Pop Music", "Pop Music"),
    ("Jazz Music", "Jazz Music"),
    ("R&B Music", "R&B Music"),
    ("Rock Music", "Rock Music"),
    ("Country Music", "Country Music"),
    ("Dance Music", "Dance Music"),
    ("Hip Hop Music", "Hip Hop Music"),
    ("Other", "Other"),
]


class Album(models.Model):
    MAX_LENGTH = 30

    album_name = models.CharField(
        max_length=MAX_LENGTH,
        null=False,
        blank=False,
        unique=True,
        # verbose_name="Album Name",
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
        # verbose_name="Image URL",
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
