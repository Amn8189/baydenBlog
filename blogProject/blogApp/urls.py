from django.urls import path
from .views import Homepage, Article_content

urlpatterns = [
    path('', Homepage, name="homepage"),
    path('article/<int:id>', Article_content, name="article"),
]