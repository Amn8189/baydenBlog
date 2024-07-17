from django.urls import path
from .views import Homepage, Article_content, search, savedComment, createArticle

urlpatterns = [
    path('', Homepage, name="homepage"),
    path('article/<int:id>', Article_content, name="article"),
    path('search/', search, name="search"),
    path('savedComment/<int:id>', savedComment, name="savedComment"),
    path('createArticle/', createArticle, name="createArticle"),
]