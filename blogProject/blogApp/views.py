from django.shortcuts import render
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

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
    
def updateArticle(request, id):
    # Fetch the artcle being updated
    article = Article.objects.get(pk=id)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES["image"]
        # Re-write the content with new content
        article.title = title
        article.content = content
        article.image = image
        # Save
        article.save()
    return render(request, "updateArticle.html", {"article": article})

def deleteArticle(request, id):
    article_instance = Article.objects.get(pk=id)
    if request.method == "POST":
        article_instance.delete()
        return redirect("homepage")
    return render(request, "deleteArticle.html", {"article" : article_instance})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"