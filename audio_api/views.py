# audio_api/views.py
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import action # Importa action
from django.http import FileResponse, Http404 # Importa FileResponse y Http404


from .models import AudioFile
from .serialaizers import AudioFileSerializer

class AudioFileViewSet(viewsets.ModelViewSet):
    queryset = AudioFile.objects.all()
    serializer_class = AudioFileSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['get']) # Esto crea una nueva acción para el detalle (un objeto específico)
    def download(self, request, pk=None):
        try:
            audio_file_obj = self.get_object() # Obtiene el objeto AudioFile por su PK
        except Http404:
            return Response({"detail": "Audio file not found."}, status=status.HTTP_404_NOT_FOUND)

        file_path = audio_file_obj.audio_file.path # Obtiene la ruta física del archivo
        
        try:
            # open(file_path, 'rb') abre el archivo en modo binario de lectura
            # filename=os.path.basename(file_path) sugiere un nombre de archivo para la descarga
            # content_type se infiere o puedes especificarlo (e.g., 'audio/mpeg' para MP3)
            response = FileResponse(open(file_path, 'rb'), filename=audio_file_obj.audio_file.name)
            # Opcional: Si quieres forzar la descarga en lugar de la reproducción en el navegador
            # response['Content-Disposition'] = f'attachment; filename="{audio_file_obj.audio_file.name}"'
            
            # DRF intentará inferir el Content-Type, pero puedes forzarlo si lo conoces
            # import mimetypes
            # content_type, encoding = mimetypes.guess_type(file_path)
            # if content_type:
            #     response['Content-Type'] = content_type

            return response
        except FileNotFoundError:
            return Response({"detail": "File not found on server storage."}, status=status.HTTP_404_NOT_FOUND)
        
    @api_view(['get'])
    def ultimo_audio(request):
        ultimo = AudioFile.objects.order_by('-uploaded_at').first()
        if not ultimo:
            return Response({'detail': 'No hay audios grabados'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AudioFileSerializer(ultimo, context={'request': request})
        return Response(serializer.data)
    @api_view(['get'])
    def to_mp3(request,id):
        audio= AudioFile.objects.get(id=id)
        try:
            mp3_path = audio.to_mp3()  # Llama al método to_mp3 del modelo AudioFile
            return Response({"message": "Audio converted to MP3 successfully.", "mp3_path": mp3_path}, status=status.HTTP_200_OK)
        except EnvironmentError as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    @api_view(['get'])
    def to_wav(request,id):
        audio= AudioFile.objects.get(id=id)
        try:
            wav_path = audio.to_wav()  # Llama al método to_wav del modelo AudioFile
            return Response({"message": "Audio converted to WAV successfully.", "wav_path": wav_path}, status=status.HTTP_200_OK)
        except EnvironmentError as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)