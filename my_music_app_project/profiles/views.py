from django.urls import reverse_lazy
from django.views import generic as views

from my_music_app_project.albums.models import Album
from my_music_app_project.common.views import get_current_profile
from my_music_app_project.profiles.models import Profile


class ProfileDetails(views.DetailView):
    queryset = Profile.objects.all()
    template_name = "profile/profile-details.html"

    def get_object(self, queryset=None):
        return get_current_profile()
        # return queryset.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["albums_count"] = self.get_object().profile_albums.count()

        return context


class ProfileDelete(views.DeleteView):
    model = Profile
    fields = "__all__"
    template_name = "profile/profile-delete.html"
    success_url = reverse_lazy("home page")

    def get_object(self, queryset=None):
        return get_current_profile()


