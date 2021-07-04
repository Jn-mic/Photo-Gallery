from django.contrib import admin
from . models import Editor,Article, tag

# Register your models here.
admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tag)