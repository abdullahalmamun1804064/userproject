from django.contrib import admin
from . models import blog
class blg(admin.ModelAdmin):
    list_display=['title','disc']
admin.site.register(blog,blg)
