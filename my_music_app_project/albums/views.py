from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from my_music_app_project.albums.forms import DeleteAlbumForm
from my_music_app_project.albums.models import Album
from my_music_app_project.common.views import get_current_profile
from my_music_app_project.profiles.models import Profile


class CreateAlbumView(views.CreateView):
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


class DetailsAlbumView(views.DetailView):
    model = Album
    template_name = "album/album-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_profile"] = get_current_profile()

        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #
    #     album_pk = self.request.GET.get("pk", None)
    #     if album_pk is not None:
    #         queryset = queryset.filter(pk=album_pk)
    #
    #     return queryset


class EditAlbumView(views.UpdateView):
    model = Album
    fields = ["album_name", "artist", "genre", "description", "image_url", "price"]
    template_name = "album/album-edit.html"
    success_url = reverse_lazy("home page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_profile"] = get_current_profile()

        return context

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


class DeleteAlbumView(views.DeleteView):
    model = Album
    # form_class = DeleteAlbumForm
    template_name = "album/album-delete.html"
    success_url = reverse_lazy("home page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_profile"] = get_current_profile()
        context["form"] = DeleteAlbumForm(instance=self.get_object())

        return context







