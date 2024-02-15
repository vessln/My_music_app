from django.urls import path

from my_music_app_project.profiles.views import ProfileDetails, ProfileDelete

urlpatterns = (
    path("details/", ProfileDetails.as_view(), name="profile details"),
    path("delete/", ProfileDelete.as_view(), name="profile delete"),
)