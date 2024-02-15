from django.urls import path, include

from my_music_app_project.albums.views import CreateAlbumView, DetailsAlbumView, EditAlbumView, DeleteAlbumView

urlpatterns = (
    path("add/", CreateAlbumView.as_view(), name="create album"),
    path("<int:pk>/", include([
                         path("details/", DetailsAlbumView.as_view(), name="details album"),
                         path("edit/", EditAlbumView.as_view(), name="edit album"),
                         path("delete/", DeleteAlbumView.as_view(), name="delete album"),
            ]),
         ),

)