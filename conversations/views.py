import hashlib
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Conversation
from .serializers import ConversationSerializer
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
from rest_framework.pagination import PageNumberPagination

from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import File
from .serializers import FileSerializer

class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_hash = hashlib.md5(request.data['upload'].read()).hexdigest()
            request.data['upload'].seek(0)
            if File.objects.filter(file_hash=file_hash).exists():
                return Response({'error': 'File already exists'}, status=status.HTTP_400_BAD_REQUEST)
            file_serializer.save(file_hash=file_hash)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDeleteView(generics.DestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class ConversationPagination(PageNumberPagination):
    page_size = 10

class ConversationList(generics.ListAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['participant', 'date']
    pagination_class = ConversationPagination
