from rest_framework import serializers
from .models import ComicBook, Character, CharacterAppearance
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user

class ComicBookSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ComicBook
        fields = '__all__'
    

class CharacterSerializer(serializers.ModelSerializer):
    comic_books = ComicBookSerializer(many=True, read_only=True)
    class Meta:
        model = Character
        fields = '__all__'

class CharacterAppearanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterAppearance
        fields = '__all__'
        read_only_fields = ('comic_book',)