from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from my_music_app_project.albums.models import Album
from my_music_app_project.common.views import get_current_profile
from my_music_app_project.profiles.models import Profile


class CreateAlbum(views.CreateView):
    model = Album
    fields = ["album_name", "artist", "genre", "description", "image_url", "price"]
    template_name = "album/album-add.html"
    success_url = reverse_lazy("home page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_profile"] = get_current_profile()

        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["album_name"].label = "Album Name"
        form.fields['image_url'].label = "Image URL"

        form.fields["album_name"].widget.attrs["placeholder"] = "Album Name"
        form.fields["artist"].widget.attrs["placeholder"] = "Artist"
        form.fields["description"].widget.attrs["placeholder"] = "Description"
        form.fields["image_url"].widget.attrs["placeholder"] = "Image URL"
        form.fields["price"].widget.attrs["placeholder"] = "Price"

        return form

    def form_valid(self, form):
        form.instance.owner = Profile.objects.first()
        return super().form_valid(form)


class DetailsAlbum(views.DetailView):
    model = Album
    fields = "__all__"
    template_name = "album/album-details.html"

    def get_object(self, queryset=None):
        return Album.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["album"] = Album.objects.first()

        return context


class EditAlbum(views.UpdateView):
    model = Album
    fields = "__all__"
    template_name = "album/album-edit.html"


class DeleteAlbum(views.DeleteView):
    model = Album
    fields = "__all__"
    template_name = "album/album-delete.html"
