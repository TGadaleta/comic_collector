from rest_framework import serializers
from .models import ComicBook

class ComicBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComicBook
        fields = '__all__'