from django.db import models
from pydub import AudioSegment
from pydub.utils import which
import librosa
import re
import soundfile as sf

class AudioFile(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    audio_file = models.FileField(upload_to='audio/') # Files will be stored in media/audio/
    uploaded_at = models.DateTimeField(auto_now_add=True)
    cuantizacion= models.IntegerField(blank=True,null=True) # Cuantization level, e.g., 16 for 16-bit audio
    tasa_muestreo =models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title if self.title else f"Audio File {self.id}"
    def to_mp3(self,rate):
        # Ensure ffmpeg is available
        AudioSegment.converter = which("ffmpeg")
        if not AudioSegment.converter:
            raise EnvironmentError("FFmpeg is not installed or not found in the system PATH.")


        # Load the audio file
        #audio = AudioSegment.from_file(self.audio_file.path)
        y,sr = librosa.load(self.audio_file.path,sr=None)
        y_resampled = librosa.resample(y, orig_sr=sr,target_sr=rate)  # Resample the audio to the specified rate
        
        sf.write(re.sub(r'\.[a-zA-Z0-9]+$','.mp3',self.audio_file.path), y_resampled, rate,format='mp3')  # Export to MP3 with the specified sample rate
        #mp3=y_resampled.export(re.sub(r'\.[a-zA-Z0-9]+$','.mp3',self.audio_file.path), format='mp3')  # Export to MP3 with the specified sample rate
        nombre=re.sub(r'\.[a-zA-Z0-9]+$','.mp3',self.audio_file.path)
        # Save the exported MP3 file
        AudioFile.objects.create(title=self.title, audio_file=nombre, uploaded_at=self.uploaded_at,tasa_muestreo=rate, cuantizacion=16)  # Assuming 16-bit quantization for MP3
        return nombre  # Return the name of the exported MP3 file
    def to_wav(self,rate):
        # Ensure ffmpeg is available
        AudioSegment.converter = which("ffmpeg")
        if not AudioSegment.converter:
            raise EnvironmentError("FFmpeg is not installed or not found in the system PATH.")

        # Load the audio file
        audio = AudioSegment.from_file(self.audio_file.path)

        wav_path = re.sub(r'\.[a-zA-Z0-9]+$', '.wav', self.audio_file.path)
        AudioFile.objects.create(title=self.title+'to_wav', audio_file=wav_path, uploaded_at=self.uploaded_at)
        audio.export(wav_path, format='wav')

        