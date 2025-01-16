from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class ComicBook(models.Model):
    title = models.CharField(max_length=100)
    issue_number = models.IntegerField()
    description = models.TextField()
    release_date = models.DateField()
    page_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Character(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=250)
    comic_books = models.ManyToManyField(ComicBook)

    def __str__(self):
        return self.name
    
class CharacterAppearance(models.Model):
    comic_book = models.ForeignKey(ComicBook, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    appearance_type = models.CharField(
        max_length=50,
        choices=[
            ('main', 'Main Role'),
            ('cameo', 'Cameo'),
            ('first', 'First Appearance'),
        ],
        default='main'
    )