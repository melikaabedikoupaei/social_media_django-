from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','id_user','location')
    list_filter=('location',)
    ordering=["id_user"]
    search_fields=('user','id_user','location')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('user','created_at','no_of_likes')
    search_fields=('user','created_at','no_of_likes')
admin.site.register(LikePost)
admin.site.register(FollowersCount)