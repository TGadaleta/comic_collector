from django.contrib import admin

# Register your models here.
from .models import ComicBook, Character, CharacterAppearance

admin.site.register(ComicBook)
admin.site.register(Character)
admin.site.register(CharacterAppearance)