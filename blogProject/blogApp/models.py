from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class Author(admin.ModelAdmin):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/articles', default="media/KuaZoneVB.jpg")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    publish_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['publish_date']

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content