from .models import Article
from django.contrib.sitemaps import Sitemap

class ArticleSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    
    def items(self):
        return Article.objects.all()
    
    def lastmod(self, one_article):
        return one_article.updated