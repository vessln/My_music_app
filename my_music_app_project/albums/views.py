from django.urls import reverse_lazy
from django.views import generic as views

from my_music_app_project.albums.forms import DeleteAlbumForm
from my_music_app_project.albums.models import Album
from my_music_app_project.common.views import get_current_profile
from my_music_app_project.profiles.models import Profile


class PrefilledFormViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["album_name"].label = "Album Name"  # or verbose_name="Album Name" (in model's field 'album_name')
        form.fields['image_url'].label = "Image URL"  # or verbose_name="Image URL" (in model's field 'image_url')

        form.fields["album_name"].widget.attrs["placeholder"] = "Album Name"
        form.fields["artist"].widget.attrs["placeholder"] = "Artist"
        form.fields["description"].widget.attrs["placeholder"] = "Description"
        form.fields["image_url"].widget.attrs["placeholder"] = "Image URL"
        form.fields["price"].widget.attrs["placeholder"] = "Price"

        return form


class CreateAlbumView(PrefilledFormViewMixin, views.CreateView):
    queryset = Album.objects.all()
    fields = ["album_name", "artist", "genre", "description", "image_url", "price"]
    template_name = "album/album-add.html"
    success_url = reverse_lazy("home page")

    def form_valid(self, form):
        form.instance.owner = get_current_profile()

        return super().form_valid(form)


class DetailsAlbumView(views.DetailView):
    queryset = Album.objects.all()
    template_name = "album/album-details.html"

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     album_pk = self.request.GET.get("pk", None)
    #     if album_pk is not None:
    #         queryset = queryset.filter(pk=album_pk)
    #
    #     return queryset


class EditAlbumView(PrefilledFormViewMixin, views.UpdateView):
    queryset = Album.objects.all()
    fields = ["album_name", "artist", "genre", "description", "image_url", "price"]
    template_name = "album/album-edit.html"
    success_url = reverse_lazy("home page")


class DeleteAlbumView(views.DeleteView):
    # model = Album
    # form_class = DeleteAlbumForm
    queryset = Album.objects.all()
    template_name = "album/album-delete.html"
    success_url = reverse_lazy("home page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_profile"] = get_current_profile()
        context["form"] = DeleteAlbumForm(instance=self.get_object())

        return context

    # def get_form_kwargs(self):  # to prefill current form with data from DB
    #     kwargs = super().get_form_kwargs()
    #     kwargs["instance"] = self.object
    #     return kwargs

