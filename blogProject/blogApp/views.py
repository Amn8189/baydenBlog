from django.shortcuts import render
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

# Create your views here.
def Homepage(request):
    Objects = Article.objects.all()
    return render(request,'homepage.html', {"articles": Objects})

def Article_content(request, id):
    article = Article.objects.get(pk=id)
    comments = article.comments.all()
    return render(request, 'content.html', {"article": article, "comments" : comments})

def search(request):
    query = request.POST.get("query")
    filtered_articles = Article.objects.filter(title__contains=query)
    return render(request, "search.html", {"article": filtered_articles})

def savedComment(request, id):
    typedComment = request.POST.get("comment")
    article_instance = Article.objects.get(pk=id)
    newComment = Comment.objects.create(name="anonymous", content=typedComment, article=article_instance)
    newComment.save()
    allComments = article_instance.comments.all().order_by("-comment_date")
    return render(request, "comments.html",  {"allComments": allComments})

@login_required

def createArticle(request:HttpRequest):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES["image"]
        author = request.user
        # SAVE
        new_article = Article.objects.create(title=title, content=content, image=image, author=author)
        new_article.save()
    return render(request, "createArticle.html")
    