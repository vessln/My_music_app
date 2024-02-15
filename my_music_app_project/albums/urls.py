from django.urls import path, include

from my_music_app_project.albums.views import CreateAlbum, DetailsAlbum, EditAlbum, DeleteAlbum

urlpatterns = (
    path("add/", CreateAlbum.as_view(), name="create album"),
    path("<int:pk>/", include([
                         path("details/", DetailsAlbum.as_view(), name="details album"),
                         path("edit/", EditAlbum.as_view(), name="edit album"),
                         path("delete/", DeleteAlbum.as_view(), name="delete album"),
            ]),
         ),

)