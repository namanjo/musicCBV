from django.urls import path

from music import views


app_name = 'music'

urlpatterns = [
    #/music/
    path('', views.IndexView.as_view(), name='index'),

    path('register', views.UserFormView.as_view(), name='register'),

    path('login', views.ForLogin.as_view(), name='login'),

    path('logout', views.ForLogout.as_view(), name='logout'),

    #/music/<album_id>/
    path('<int:pk>/', views.DetailView.as_view(), name='myalbum'),  # '<int: variable_id>/' is a change in django 2+, eg: /polls/5/

    #/music/album/add
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    #/music/<album_id>/create_song
    path('<int:pk>/create-song/', views.SongCreate.as_view(), name='create-song'),

    # /music/album/2/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

]


