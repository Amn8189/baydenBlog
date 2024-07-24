from django.urls import path
from .views import Homepage, Article_content, search, savedComment, createArticle, updateArticle, deleteArticle

urlpatterns = [
    path('', Homepage, name="homepage"),
    path('article/<int:id>', Article_content, name="article"),
    path('search/', search, name="search"),
    path('savedComment/<int:id>', savedComment, name="savedComment"),
    path('createArticle/', createArticle, name="createArticle"),
    path('updateArticle/<int:id>', updateArticle, name="updateArticle"),
    path('deleteArticle/<int:id>', deleteArticle, name="deleteArticle"),
]