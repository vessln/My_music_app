from django.core.exceptions import ValidationError


def validator_letters_numbers_underscores_in_username(value):
    for char in value:
        if not (char.isalnum() or char == "_"):
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
