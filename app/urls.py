from django.urls import path
from . import views

urlpatterns = [
    path('playlist/', views.playlist_view, name='playlist'),
    path('add_to_playlist/', views.add_to_playlist, name='add_to_playlist'),
    path('get_playlist/', views.get_playlist, name='get_playlist'),
]