from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import ComicBook
from .serializers import ComicBookSerializer

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