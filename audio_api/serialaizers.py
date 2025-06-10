# audio_api/serializers.py
from rest_framework import serializers
from .models import AudioFile

class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = ['id', 'title', 'audio_file', 'uploaded_at']
        read_only_fields = ['uploaded_at'] # Automatically set on creation