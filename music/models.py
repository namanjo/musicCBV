from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Album(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    artist = models.CharField(max_length=20)
    album_title = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    album_logo = models.FileField(max_length=200)

    def get_absolute_url(self):
        return reverse('music:myalbum', kwargs={'pk': self.pk})

    def __str__(self):
        return self.artist + " - " + self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=20)
    audio_file = models.FileField(default='')

    def get_absolute_url(self):
        return reverse('music:myalbum', kwargs={'pk': self.album_id})


    def __str__(self):
        return self.file_name