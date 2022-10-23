from django.contrib import admin
from .models import Role,Profile,AccessLevel,UserAccessLevel


class RoleAdmin(admin.ModelAdmin):
    fields = ['title','description',]
    list_display = ['pk','title','description',]
    search_fields = ['title','description',]
    list_filter = ['title','description',]
    
class ProfileAdmin(admin.ModelAdmin):
    fields = ["user","jensiat","role","phone_number","birth_date"]
    list_display = ['pk',"jensiat","user","role","phone_number","birth_date"]
    search_fields = ["user","jensiat","phone_number","birth_date"]
    list_filter = []
    
class AccessLevelAdmin(admin.ModelAdmin):
    fields = ["id","title","description"]
    list_display = ["id","title","description"]
    search_fields = ["id","title","description"]
    list_filter = ["id","title","description"]
    
class UserAccessLevelAdmin(admin.ModelAdmin):
    fields = ["user","access_level"]
    list_display = ["user","access_level"]
    search_fields = ["user","access_level"]
    list_filter = ["user","access_level"]

    autocomplete_fields  =['user']
    

admin.site.register(Role, RoleAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(AccessLevel, AccessLevelAdmin)
admin.site.register(UserAccessLevel, UserAccessLevelAdmin)


