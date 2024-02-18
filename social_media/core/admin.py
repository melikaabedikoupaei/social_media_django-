from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','id_user','location')
    list_filter=('location',)
    ordering=["id_user"]
    search_fields=('user','id_user','location')
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)