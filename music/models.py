from django.db import models

# Create your models here.


# let album Red has Primary key 1
class Album(models.Model) :
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def __str__(self):
        return self.artist + '_' + self.album_title

class Song(models.Model) :
    album = models.ForeignKey(Album , on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title