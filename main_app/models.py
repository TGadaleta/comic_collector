from django.db import models

# Create your models here.
class ComicBook(models.Model):
    title = models.CharField(max_length=100)
    issue_number = models.IntegerField()
    description = models.TextField()
    release_date = models.DateField()
    page_count = models.IntegerField()

    def __str__(self):
        return self.title