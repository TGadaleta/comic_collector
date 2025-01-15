from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import ComicBook, Character, CharacterAppearance
from .serializers import ComicBookSerializer, CharacterSerializer, CharacterAppearanceSerializer

class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the comic-collector api home route!'}
        return Response(content)

class ComicBookList(generics.ListCreateAPIView):
    queryset = ComicBook.objects.all()
    serializer_class = ComicBookSerializer

class ComicBookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComicBook.objects.all()
    serializer_class = ComicBookSerializer
    lookup_field = 'id'

class CharacterListCreate(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = 'id'

class CharacterAppearanceList(generics.ListCreateAPIView):
    serializer_class = CharacterAppearanceSerializer
    
    def get_queryset(self):
        comic_book_id = self.kwargs['comic_book_id']
        return CharacterAppearance.objects.filter(comic_book_id=comic_book_id)
    
    def perform_create(self, serializer):
        comic_book_id = self.kwargs['comic_book_id']
        comic_book = ComicBook.objects.get(id=comic_book_id)
        serializer.save(comic_book=comic_book)

class CharacterAppearanceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CharacterAppearanceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        comic_book_id = self.kwargs['comic_book_id']
        return CharacterAppearance.objects.filter(comic_book_id=comic_book_id)