from models import Article
from django.contrib.auth.models import User

user = User.objects.get(username="blogAdmin")
article = Article(title="firstArticle", content="This is the first article", author=user)
article.save()