from django.urls import path
from .views import Home, ComicBookList, ComicBookDetail, CharacterListCreate, CharacterDetail, CharacterAppearanceList, CharacterAppearanceDetail, AddCharacterToComicBook

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('comicbooks/', ComicBookList.as_view(), name='comicbook-list'),
    path('comicbooks/<int:id>/', ComicBookDetail.as_view(), name='comicbook-detail'),
    path('characters/', CharacterListCreate.as_view(), name='character-list'),
    path('characters/<int:id>/', CharacterDetail.as_view(), name='character-detail'),
    path('comicbooks/<int:comic_book_id>/characterappearances/', CharacterAppearanceList.as_view(), name='character-appearance-list'),
    path('comicbooks/<int:comic_book_id>/characterappearances/<int:id>/', CharacterAppearanceDetail.as_view(), name='character-appearance-detail'),
    path('comicbooks/<int:comic_book_id>/characters/<int:character_id>/', AddCharacterToComicBook.as_view(), name='add-character-to-comic-book'),
]