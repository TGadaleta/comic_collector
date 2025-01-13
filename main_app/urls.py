from django.urls import path
from .views import Home, ComicBookList, ComicBookDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('comicbooks/', ComicBookList.as_view(), name='comicbook-list'),
    path('comicbooks/<int:id>/', ComicBookDetail.as_view(), name='comicbook-detail'),
]