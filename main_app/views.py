from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import generics, status, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.tokens import RefreshToken
from .models import ComicBook, Character, CharacterAppearance
from .serializers import ComicBookSerializer, CharacterSerializer, CharacterAppearanceSerializer, UserSerializer

class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the comic-collector api home route!'}
        return Response(content)

class ComicBookList(generics.ListCreateAPIView):
    serializer_class = ComicBookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ComicBook.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ComicBookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ComicBookSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return ComicBook.objects.filter(user=user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response({
            'comic_book': serializer.data,
        })

class CharacterListCreate(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        comic_books_not_associated = ComicBook.objects.exclude(id__in=instance.comic_books.all())
        comic_books_serializer = ComicBookSerializer(comic_books_not_associated, many=True)

        return Response({
            'comic_book': serializer.data,
            'comic_books_not_associated': comic_books_serializer.data
        })

class CharacterAppearanceList(generics.ListCreateAPIView):
    serializer_class = CharacterAppearanceSerializer
    
    def get_queryset(self):
        comic_book_id = self.kwargs['comic_book_id']
        return CharacterAppearance.objects.filter(comic_book_id=comic_book_id)
    
    def perform_create(self, serializer):
        comic_book_id = self.kwargs['comic_book_id']
        comic_book = ComicBook.objects.get(id=comic_book_id)
        serializer.save(comic_book=comic_book)

    def perform_update(self, serializer):
        comic_book = self.get_object()
        if comic_book.user != self.request.user:
            raise PermissionDenied({'message': 'You do not have permission to edit this comic book.'})
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied({'message': 'You do not have permission to delete this comic book'})
        instance.delete()

class CharacterAppearanceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CharacterAppearanceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        comic_book_id = self.kwargs['comic_book_id']
        return CharacterAppearance.objects.filter(comic_book_id=comic_book_id)
    
class AddCharacterToComicBook(APIView):
    def post(self, request, character_id, comic_book_id):
        character = Character.objects.get(id=character_id)
        comic_book = ComicBook.objects.get(id=comic_book_id)
        character.comic_books.add(comic_book)
        return Response({ 'message': f"Comic Book {comic_book.title} added to Character {character.name}."})
    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': response.data
        })
    
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(username=request.user)
        refresh = RefreshToken.for_user(request.user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })