from django.contrib import admin

# Register your models here.
from .models import ArticlesModel,Comment


class CommentInline(admin.TabularInline):
    model = Comment
    # extra = 0
    
    
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

admin.site.register(ArticlesModel,ArticleAdmin)
admin.site.register(Comment)