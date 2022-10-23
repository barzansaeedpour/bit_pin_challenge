from django.contrib import admin

from django.contrib import admin
from .models import Score
# Register your models here.



class ScoreAdmin(admin.ModelAdmin):
    fields = ['user','content','score']
    list_display = ['user','content','score']
    search_fields = ['user','content','score']



admin.site.register(Score,ScoreAdmin)