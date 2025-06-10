from django.db import models

class AudioFile(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    audio_file = models.FileField(upload_to='audio/') # Files will be stored in media/audio/
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Audio File {self.id}"