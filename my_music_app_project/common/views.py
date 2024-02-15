from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from my_music_app_project.albums.models import Album
from my_music_app_project.profiles.models import Profile


def get_current_profile():
    profile = Profile.objects.get() or None

    return profile


class HomePageView(views.TemplateView):
    def get(self, request, *args, **kwargs):
        profile = get_current_profile()

        if profile is None:
            return HomeNoProfilePageView.as_view()(request)

        return HomeWithProfilePageView.as_view()(request)


class HomeNoProfilePageView(views.CreateView):
    model = Profile
    fields = "__all__"
    template_name = "common/home-no-profile.html"
    success_url = reverse_lazy("home page")

    # def get_success_url(self):
    #     return redirect(request.META["HTTP_REFERER"])

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["username"].widget.attrs["placeholder"] = "Username"
        form.fields["email"].widget.attrs["placeholder"] = "Email"
        form.fields["age"].widget.attrs["placeholder"] = "Age"

        return form


class HomeWithProfilePageView(views.ListView):
    model = Album
    fields = "__all__"
    template_name = "common/home-with-profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_profile"] = get_current_profile()

        return context






