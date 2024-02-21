from django import forms

from my_music_app_project.albums.models import Album


def _make_fields_readonly(readonly_fields):
    for field_name, field in readonly_fields.items():
        field.widget.attrs["readonly"] = "readonly"
        field.widget.attrs["disabled"] = "disabled" #  + override form_valid() in DeleteView


class DeleteAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ("album_name", "artist", "genre", "description", "image_url", "price")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _make_fields_readonly(self.fields)


