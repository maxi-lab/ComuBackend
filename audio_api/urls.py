# audio_api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AudioFileViewSet  # <-- Esta línea solo funciona si ultimo_audio está definido

router = DefaultRouter()
router.register(r'audio', AudioFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ultimo-audio/', AudioFileViewSet.ultimo_audio, name='ultimo-audio'),
]