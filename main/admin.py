from django.contrib import admin
from jab.main.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)

admin.site.register(Post, PostAdmin)
