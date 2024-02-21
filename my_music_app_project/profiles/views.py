from django.urls import reverse_lazy
from django.views import generic as views

from my_music_app_project.albums.models import Album
from my_music_app_project.common.views import get_current_profile
from my_music_app_project.profiles.models import Profile


class ProfileDetails(views.DetailView):
    model = Profile
    fields = "__all__"
    template_name = "profile/profile-details.html"

    def get_object(self, queryset=None):
        return get_current_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["albums_count"] = Album.objects.all().count()
        context["current_profile"] = get_current_profile()

        return context


class ProfileDelete(views.DeleteView):
    model = Profile
    fields = "__all__"
    template_name = "profile/profile-delete.html"
    success_url = reverse_lazy("home page")

    def get_object(self, queryset=None):
        return get_current_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_profile"] = get_current_profile()

        return context

