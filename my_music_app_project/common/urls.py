from django.urls import path

from my_music_app_project.common.views import HomePage

urlpatterns = (
    path("", HomePage.as_view(), name="home page"),

)