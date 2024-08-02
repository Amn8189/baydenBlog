from django.contrib import admin
from .models import Article, Author
from django.contrib.auth.admin import UserAdmin
from .forms import AuthorChangeForm, AuthorCreationForm

# OUR ADMIN IS ALSO AN AUTHOR MODEL
# HENCE WE HAVE TO TELL DJANGO THIS
class CustomAdmin(UserAdmin):
    # Which form will you use when creating a superuser
    add_form = AuthorCreationForm
    form = AuthorChangeForm
    model = Author
    list_display = ['username']
    
admin.site.register(Author, CustomAdmin)

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'updated')
    
                                       