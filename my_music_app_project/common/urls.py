from django.urls import path

from my_music_app_project.common.views import HomePageView, HomeNoProfilePageView

urlpatterns = (
    path("", HomePageView.as_view(), name="home page"),
    path("create-profile/", HomeNoProfilePageView.as_view(), name="create profile"),

)