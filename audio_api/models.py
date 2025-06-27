from django.db import models
from pydub import AudioSegment
from pydub.utils import which
import re

class AudioFile(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    audio_file = models.FileField(upload_to='audio/') # Files will be stored in media/audio/
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Audio File {self.id}"
    def to_mp3(self):
        # Ensure ffmpeg is available
        AudioSegment.converter = which("ffmpeg")
        if not AudioSegment.converter:
            raise EnvironmentError("FFmpeg is not installed or not found in the system PATH.")


        # Load the audio file
        audio = AudioSegment.from_file(self.audio_file.path)

        

        mp3=audio.export(re.sub(r'\.[a-zA-Z0-9]+$','.mp3',self.audio_file.path), format='mp3')
        
        print(mp3)
        # Save the exported MP3 file
        AudioFile.objects.create(title=self.title, audio_file=mp3.name, uploaded_at=self.uploaded_at)
        return mp3.name  # Return the name of the exported MP3 file