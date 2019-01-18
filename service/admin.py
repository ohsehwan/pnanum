import datetime
from django.contrib import admin

from service.models import Article, msch

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(msch)
class mschAdmin(admin.ModelAdmin):
    pass



