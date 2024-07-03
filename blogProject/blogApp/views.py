from django.shortcuts import render
from .models import Article

# Create your views here.
def Homepage(request):
    Objects = Article.objects.all()
    return render(request,'homepage.html', {"articles": Objects})

def Article_content(request, id):
    article = Article.objects.get(pk=id)
    return render(request, 'content.html', {"article": article})

def search(request):
    query = request.POST.get("query")
    filtered_articles = Article.objects.filter(title__contains=query)
    return render(request, "search.html", {"article": filtered_articles})