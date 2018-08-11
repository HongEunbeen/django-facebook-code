from django.contrib import admin

from facebook.models import Article
from facebook.models import Page
from facebook.models import Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Page)
admin.site.register(Comment)
