from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from my_music_app_project.profiles.validators import validator_letters_numbers_underscores_in_username


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 2
    MIN_AGE_VALUE = 0

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH),
            validator_letters_numbers_underscores_in_username,
        ],
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=[MinValueValidator(MIN_AGE_VALUE)],
        null=True,
        blank=True,
    )
