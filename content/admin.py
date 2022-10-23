
from django.contrib import admin
from .models import Content
# Register your models here.



class ContentAdmin(admin.ModelAdmin):
    fields = ['title','text',]
    list_display = ['title','text',]
    search_fields = ['title','text',]



admin.site.register(Content,ContentAdmin)