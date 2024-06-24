from django.shortcuts import render
from .models import Article

# Create your views here.
def Homepage(request):
    Objects = Article.objects.all()
    return render(request,'homepage.html', {"articles": Objects})

def Article_content(request, id):
    article = Article.objects.get(pk=id)
    return render(request, 'content.html', {"article": article})