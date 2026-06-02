from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='covers/')
    audio = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.title

class PlaylistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    audio = models.CharField(max_length=255)
    cover = models.CharField(max_length=255)