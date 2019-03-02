from django.db import models


class Song(models.Model):
    artist = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    audio_file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)