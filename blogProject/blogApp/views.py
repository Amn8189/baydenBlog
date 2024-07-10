from django.shortcuts import render
from .models import Article, Comment

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

def savedComment(request):
    typedComment = request.POST.get("comment")
    # article_id = request.POST.get("article_id")
    article_id = 1
    article_instance = Article.objects.get(pk=article_id)
    print(article_id)
    newComment = Comment.objects.create(name="anonymous", content=typedComment, article=article_instance)
    newComment.save()
    allComments = article_instance.comments.all().order_by("-comment_date")
    return render(request, "comments.html",  {"allComments": allComments})