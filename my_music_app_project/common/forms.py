from django import forms

from my_music_app_project.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Username"}),
            "age": forms.NumberInput(attrs={"placeholder": "Username"}),
        }

