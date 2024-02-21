from django.urls import path

from my_music_app_project.common.views import home_page, HomeNoProfilePageView

urlpatterns = (
    path("", home_page, name="home page"),
    path("create-profile/", HomeNoProfilePageView.as_view(), name="create profile"),

)