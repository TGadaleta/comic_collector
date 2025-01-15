from rest_framework import serializers
from .models import ComicBook, Character, CharacterAppearance

class ComicBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComicBook
        fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class CharacterAppearanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterAppearance
        fields = '__all__'
        read_only_fields = ('comic_book',)